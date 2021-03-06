import multiprocessing as mp
import numpy as np
import time


def my_function(i, param1, param2, param3):
    result = param1**2 * param2 + param3
    time.sleep(2)  # simulating long run
    return (i, result)


def get_result(result):
    global results
    results.append(result)


if __name__ == "__main__":
    params = (
        np.random.random((10, 3)) * 100.0
    )  # Set up an array with 3 columns of random numbers between 0 and 100.
    results = []
    ts = time.time()
    for i in range(0, params.shape[0]):
        get_result(my_function(i, params[i, 0], params[i, 1], params[i, 2]))
    print("Time in serial:", time.time() - ts)
    print(results)

    # reset, parallel version, results not in order, that's why index returned too
    results = []
    ts = time.time()
    pool = mp.Pool(mp.cpu_count())
    for i in range(0, params.shape[0]):
        pool.apply_async(
            my_function,
            args=(i, params[i, 0], params[i, 1], params[i, 2]),
            callback=get_result,
        )
    pool.close()
    pool.join()
    print("Time in parallel:", time.time() - ts)
    print(results)
