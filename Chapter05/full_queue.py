import threading
import queue
import time


def my_publisher(queue_p):
    while not queue_p.full():
        queue_p.put(1)
        print("{} Appended 1 to queue: {}".format(threading.current_thread(), queue_p.qsize()))
        time.sleep(1)


myQueue = queue.Queue()
for i in range(10):
    myQueue.put(i)

threads = []
for i in range(4):
    thread = threading.Thread(target=mySubscriber, args=(myQueue,))
    thread.start()
    threads.append(thread)

myQueue.join
