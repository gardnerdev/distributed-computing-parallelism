from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # in real code, this section might
    # read in data parameters from a file
    numData = 10

    # Note how comm.send and comm.recv have lower case s and r.
    comm.send(numData, dest=1)

    data = np.linspace(0.0, 3.14, numData)
    # Note how comm.Send and comm.Recv used to send and receive the numpy array have upper case S and R.
    comm.Send(data, dest=1)

elif rank == 1:

    numData = comm.recv(source=0)
    print("Number of data to receive: ", numData)

    data = np.empty(numData, dtype="d")  # allocate space to receive the array
    comm.Recv(data, source=0)

    print("data received: ", data)
