import threading
import time
import random


class MyThread(threading.Thread):

    def __init__(self, _barrier):
        threading.Thread.__init__(self)
        self.barrier = _barrier

    def run(self):
        print("Thread {} working on something".format(threading.current_thread()))
        time.sleep(random.randint(1, 10))
        print("Thread {} is joining {} waiting on Barrier".format(threading.current_thread(), self.barrier.n_waiting))
        self.barrier.wait()

        print("Barrier has been lifted, continuing with work")


barrier = threading.Barrier(4)

threads = []

for i in range(4):
    thread = MyThread(barrier)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()
