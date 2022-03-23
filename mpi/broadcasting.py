from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {"key1": [1, 2, 3], "key2": ("abc", "xyz")}
else:
    data = None

# Broadcasting takes a variable and sends an exact copy of it to all processes on a communicator
data = comm.bcast(data, root=0)
print("Rank: ", rank, ", data: ", data)
