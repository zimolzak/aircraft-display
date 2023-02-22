from mpi4py import MPI
wsize = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
print("Hello from rank " + str(rank) + " of " + str(wsize))
