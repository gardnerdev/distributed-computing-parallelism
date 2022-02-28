import time
from multiprocessing import Process

def cube(x):
    print(f"starting process {x}")
    print(f"calculating cube of {x}... result: {x*x*x}")
    time.sleep(1)
    print(f"end process {x}")
    

if __name__ =="__main__":
    processes = []
    for i in range(5):
        p = Process(target=cube, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
        
    