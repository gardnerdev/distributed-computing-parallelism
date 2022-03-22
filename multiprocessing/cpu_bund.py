import time



def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)



if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    # This code calls cpu_bound() 20 times with a different large number each time. 
    # It does all of this on a single thread in a single process on a single CPU.
    st = time.time()
    find_sums(numbers)
    duration = time.time() - st
    print(f"Duration {duration} seconds")