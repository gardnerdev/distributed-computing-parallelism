from mpi4py import MPI

comm = (
    MPI.COMM_WORLD
)  # get information about all the processors available to run your script
size = (
    comm.Get_size()
)  # size gives the total number of ranks, or processors, allocated to run our scrip
rank = (
    comm.Get_rank()
)  # rank gives the identifier of the processor currently executing the code

print(
    f"Hello world from rank {rank} of {size}"
)  # print statement will print once for each processor used in the job.
