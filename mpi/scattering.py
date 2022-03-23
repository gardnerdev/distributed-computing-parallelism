from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    # restrictions to scatter, and that is that you can only scatter as many elements as you have processors.
    data = [(x + 1) ** x for x in range(size)]
    print(f"we will be scattering: {data}")
else:
    data = None

data = comm.scatter(data, root=0)
print(f"rank {rank}  has data:, {data}")
