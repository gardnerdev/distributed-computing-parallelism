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
        p = Process(target=cube, args=(i,)) # target specified the function to be called
        processes.append(p)
        p.start() # start the process
    
    for p in processes: # all processes looped over to wait until every process execution is complete, which
        p.join()        # is detected using the join() method. It helps in making sure that the rest of the 
                        # program runs only after the multiprocessing is complete
        
    