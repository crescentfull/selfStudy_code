import random
import threading
import time


def working():
    max([random.random() for i in range(500000000)])


# 1 Thread
s_time = time.time()
working()
working()
e_time = time.time()
print(f'{e_time - s_time:.5f}')


# 2 Threads
s_time = time.time()
threads = []
for i in range(2):
    threads.append(threading.Thread(target=working))
    threads[-1].start()

for t in threads:
    t.join()

e_time = time.time()
print(f'{e_time - s_time:.5f}')