import time
from multiprocessing import Pool


def cube(x):
    print(f"start process {x}")
    result = x * x * x
    # time.sleep(1)
    print(f"end process {x}")
    return result


if __name__ == "__main__":
    ts = time.time()
    pool = Pool(processes=4)
    print([pool.apply(cube, args=(x,)) for x in range(10)]) # apply() method blocks the primary process until all the processes are complete
    pool.close()                                            # it accepts multiple arguments, maintains the order of the result, and isn’t concurrent
    pool.join()
    print("Time in parallel:", time.time() - ts)
