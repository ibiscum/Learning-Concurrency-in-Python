import threading
import queue
import time


def my_subscriber(queue_p):
    time.sleep(1)
    while not queue_p.empty():
        item = queue_p.get()
        if item is None:
            break
        print("{} removed {} from the queue".format(threading.current_thread(), item))
        queue_p.task_done()


myQueue = queue.Queue()
for i in range(5):
    myQueue.put(i)

print("Queue Populated")

thread = threading.Thread(target=my_subscriber, args=(myQueue,))
thread.start()

print("Not Progressing Till Queue is Empty")
myQueue.join()
print("Queue is now empty")
