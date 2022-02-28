from multiprocessing import Process, Pipe

def cube_sender(x, x_conn):
    print(f"Sending value...")
    x_conn.send(x * x * x)

def cube_receiver(y_conn):
    print(f"Receiving value...")
    print(y_conn.recv())
    

if __name__ == "__main__":
    x_conn, y_conn = Pipe()
    processes = []
    
    p1 = Process(target=cube_sender,args=(5, x_conn))
    
    p2 =  Process(target=cube_receiver,args=(y_conn,))
    
    
    processes.extend([p1, p2])
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()