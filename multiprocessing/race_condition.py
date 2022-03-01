import concurrent.futures


counter = 0


def increment_counter(fake_value):
    global counter
    for _ in range(10):
        counter += 1
        print(counter)

if __name__ == "__main__":
    fake_data = [x for x in range(10)]
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
        executor.map(increment_counter, fake_data)
        