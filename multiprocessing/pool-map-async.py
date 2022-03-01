import time 
from multiprocessing import Pool

def collect_result(val):
    return val



def cube(x):
    print(f"start process {x}")
    time.sleep(1)
    print(f"end process {x}")
    return x*x*x


def cube_print(x):
    print(x * x * x)
    

if __name__ == "__main__":
    pool = Pool(processes=4)
    print(pool.map_async(cube, range(10), callback=collect_result).get())
    pool.map_async(cube_print, range(10))
    print("HERE!")                  # “HERE” and “HERE AGAIN” are written to the console when map_async() runs,
                                    #showcasing its non-blocking nature
    print("HERE AGAIN!")
    pool.close()
    pool.join()