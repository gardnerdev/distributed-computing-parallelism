from multiprocessing import Process, Queue


def cube(x, q):
    q.put(x * x * x)


def add(x, q):
    q.put(x + 1)

if __name__ == "__main__":
    q = Queue()
    processes = []
    for i in range(3):
        p = Process(target=cube, args=(i, q))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    processes = []
    print("INITIAL VALUES: ")
    while not q.empty():
        val = q.get()
        print(val)
        p = Process(target=add, args=(val, q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        
    print("FINAL VALUES: ")
    while not q.empty():
        print(q.get())  