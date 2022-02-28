from multiprocessing import Process, Pipe

def cube_sender(x, x_conn):
    print(f"Sending value...")
    x_conn.send(x * x * x) # output sent to y_conn

def cube_receiver(y_conn):
    print(f"Receiving value...")
    print(y_conn.recv()) # input of the process p, which receives the output and prints the resultant cube
    

if __name__ == "__main__":
    x_conn, y_conn = Pipe() # if two processes need to communicate, Pipe's the best choice. A pipe can 
                            # have two end-points where each has sand() and recv() methods. Data in pipe
                            # could get corrupted if two processes (threads) read from or write to the same
                            # end-point simultaneously  -> see queue.py
    processes = []
    
    # cube_sender and cube_receiver are two processes that communicate with each other using a pipe
    
    p1 = Process(target=cube_sender,args=(5, x_conn))
    
    p2 =  Process(target=cube_receiver,args=(y_conn,))
    
    
    processes.extend([p1, p2])
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()