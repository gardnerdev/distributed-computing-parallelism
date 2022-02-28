from multiprocessing import Process, Array


def cube(x):
    for i in range(len(x)):
        x[i] = x[i] + 1
        
        
        

if __name__ == "__main__":
    arr = Array("i",3) # Array() initializes an empty array possessing int data type having a length 3. 
                        # Note: `‘d’` indicates double-precision float, and `‘i’` (in Array(“i”, 3)) indicates a signed integer.
    p = Process(target=cube, args=(arr,))
    p.start()
    p.join()
    
    print(arr[:])