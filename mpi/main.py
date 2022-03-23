from mpi4py import MPI
import time
import numpy as np


def my_function(param1, param2, param3):
    result = param1**2 * param2 + param3
    time.sleep(2)
    return result


comm = (
    MPI.COMM_WORLD
)  # get information about all the processors available to run your script
size = (
    comm.Get_size()
)  # size gives the total number of ranks, or processors, allocated to run our scrip
rank = (
    comm.Get_rank()
)  # rank gives the identifier of the processor currently executing the code


params = np.random.random((15, 3)) * 100.0  # parameters to send to my_function
# I’ve specifically made the number of rows in params (15)
# oddly divisible by the number of processors (4) so that we have to do a little extra math to break up params
n = params.shape[0]

count = n // size  # number of catchments for each process to analyze
remainder = n % size  # extra catchments if n is not a multiple of size


# Now each processor has a variable indexing the start and stop locations of its chunk in the params array.
if rank < remainder:  # processes with rank < remainder analyze one extra catchment
    start = rank * (count + 1)  # index of first catchment to analyze
    stop = start + count + 1  # index of last catchment to analyze
else:
    start = rank * count + remainder
    stop = start + count


# get the portion of the array to be analyzed by each rank
local_params = params[start:stop, :]
# create result array
local_results = np.empty((local_params.shape[0], local_params.shape[1] + 1))
# write parameter values to result array
local_results[:, : local_params.shape[1]] = local_params
# run the function for each parameter set and rank
local_results[:, -1] = my_function(
    local_results[:, 0], local_results[:, 1], local_results[:, 2]
)


# send results to rank 0
if rank > 0:
    # send results to process 0
    comm.Send(local_results, dest=0, tag=14)
else:
    # initialize final results with results from process 0
    final_results = np.copy(local_results)
    # determine the size of the array to be received from each process
    for i in range(1, size):
        if i < remainder:
            rank_size = count + 1
        else:
            rank_size = count
        # create empty array to receive results
        tmp = np.empty((rank_size, final_results.shape[1]), dtype=float)
        # receive results from the process
        comm.Recv(tmp, source=i, tag=14)
        # add the received results to the final results
        final_results = np.vstack((final_results, tmp))
    print("results")
    print(final_results)
