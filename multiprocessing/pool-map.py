from re import X
import time
from multiprocessing import Pool



def cube(x):
    print(f"start process {x}")
    result = x * x * x
    time.sleep(1)
    print(f"end process {x}")
    return result


if __name__ == "__main__":
    ts = time.time()
    pool = Pool(processes=4)
    print(pool.map(cube, range(10)))    # map() method supports concurrency — doesn’t accept multiple 
                                        # arguments and blocks the main program until all the processes are complete
                                        # It also maintains the order of the result (although the computation order could differ!).
                                        # Unlike apply(), map() accepts an iterator to be passed as an argument to the function cube().
    pool.close()                        
    pool.join()                         
    print("Time in concurrent manner:", time.time() - ts)