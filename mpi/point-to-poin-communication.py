from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# pass data from one process to another.
if rank == 0:
    data = [7, 3.14, 5]
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print("On process 1, data is ", data)
