from mpi4py import MPI
import numpy as np
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
# from 1 to at most 5000 elements
list_size = random.randint(1, 5000)
# elements from scope 1<=element_generator<=1000
element_generator = random.randint(1, 1000)
if rank == 0:
    data = [element_generator for x in range(list_size)]
    # determine the size of each sub-task
    print(f"Number of elements {len(data)}")
    ave, res = divmod(len(data), nprocs)
    counts = [ave + 1 if p < res else ave for p in range(nprocs)]

    # determine the starting and ending indices of each sub-task
    starts = [sum(counts[:p]) for p in range(nprocs)]
    ends = [sum(counts[: p + 1]) for p in range(nprocs)]

    # converts data into a list of arrays
    data = [data[starts[p] : ends[p]] for p in range(nprocs)]
else:
    data = None
data = comm.scatter(data, root=0)
print("Process {} has number of elements:".format(rank), len(data))
