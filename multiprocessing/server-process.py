from multiprocessing import Process, Manager


def cube(d,l):
    d["car"] = "ford"
    l.sort()



if __name__ == "__main__":
    manager = Manager()  
    
    d = manager.dict()    # Here dictionary and list types are initialized and manipulated using the manager object.
    l = manager.list([9,3])
    
    p = Process(target=cube, args=(d,l))
    
    p.start()
    p.join()
    
    print(d)
    print(l)