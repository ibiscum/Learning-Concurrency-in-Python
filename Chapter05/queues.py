import threading
import queue
import random
import time


def my_subscriber(queue_p):
    while not queue_p.empty():
        item = queue_p.get()
        if item is None:
            break
        print("{} removed {} from the queue".format(threading.current_thread(), item))
        queue_p.task_done()
        time.sleep(1)


myQueue = queue.Queue()
for i in range(10):
    myQueue.put(i)

print("Queue Populated")

threads = []
for i in range(4):
    thread = threading.Thread(target=my_subscriber, args=(myQueue,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
