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
    for each_item in pool.imap(cube, range(10)):
        print(each_item)
    pool.close()
    pool.join()
    print("Time in concurrent manner:", time.time() - ts)