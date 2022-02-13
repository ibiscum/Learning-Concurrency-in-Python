import threading
import time
import random


def execute_thread(j):
    print("Thread {} started".format(j))
    sleep_time = random.randint(1, 10)
    time.sleep(sleep_time)
    print("Thread {} finished executing".format(j))


for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()

    print("Active Threads:", threading.enumerate())
