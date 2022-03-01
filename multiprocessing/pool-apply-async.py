from gc import collect
import time
from multiprocessing import Pool


def collect_result(val):
    return val

def cube(x):
    print(f"start process {x}")
    # time.sleep(1)
    print(f"end process {x}")
    return x * x * x


if __name__ == "__main__":
    ts = time.time()
    pool = Pool(processes=4)
    for x in range(10):
        print(pool.apply_async(cube, args=(x,), callback=collect_result).get()) # apply_async() can be used to return the value immediately 
                                                                                # after its execution is complete. 
                                                                                # This method maintains the order of the result
                                                                                # and supports concurrency.
    pool.close()
    pool.join()
    print("Time in parallel & concurrent:", time.time() - ts)