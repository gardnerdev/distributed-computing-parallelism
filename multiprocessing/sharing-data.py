from multiprocessing import Process, Value

def cube(x):
    x.value = x.value * x.value * x.value
    
    
if __name__ == "__main__":
    num = Value("i", 2)
    p = Process(target=cube, args=(num,))
    p.start()
    p.join()
    p = Process(target=cube, args=(num,))
    p.start()
    p.join()
    print(num.value)