from multiprocessing import Process, Queue
import random
import time


class Messanger:
    el_list = []

    def __init__(self, el_list):
        self.el_list = el_list

    def get_data_size(self):
        print(len(self.el_list))
        # return len(self.el_list)

    def get_item(self, index):
        print(self.el_list[index])
        # return self.el_list[index]

    def send_message(receiver, message_content, q):
        q.put({receiver: message_content})

    def receive_message(q):
        message = q.get()
        return message.values()[0]

    def record_result(self):
        distinct_set = set(self.el_list)
        q.put(distinct_set)


def chunker_list(seq, size):  # spliting entry list
    return (seq[i::size] for i in range(size))


def solution(messenger: Messanger, whoami):
    mess.record_result
    return whoami


if __name__ == "__main__":
    print("Multiprocessing version")
    # user_list = [int(x) for x in input().split()]
    user_list = [random.randint(1, 5000) for x in range(1, 1000)]
    start = time.time()
    q = Queue()
    computers = []

    for i in chunker_list(user_list, 10):
        mess = Messanger(i)
        p = Process(target=mess.record_result, args=())
        computers.append(p)
        p.start()

    for p in computers:
        p.join()

    final = []
    while not q.empty():
        final.append(set(q.get()))

    result = set()
    for x in final:
        result = result.union(x)
    print(len(result))
    end = time.time()
    print(f"time: {end - start}")

    print(f"Sequential version:")
    start = time.time()
    print(f"{len(set(user_list))}")
    end = time.time()
    print(f"time: {end - start}")
