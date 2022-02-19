import queue
import threading


def my_subscriber(queue_p):
    while True:
        item = queue_p.get()
        if item is None:
            break
        print("{} removed {} from the queue".format(threading.current_thread(), item))
        print("Queue Size is now: {}".format(queue_p.qsize()))
        queue_p.task_done()


myQueue = queue.Queue()
for i in range(10):
    myQueue.put(i)

print("Queue Populated")

threads = []
for i in range(4):
    thread = threading.Thread(target=my_subscriber, args=(myQueue,))
    thread.start()
    threads.append(thread)

myQueue.join()
