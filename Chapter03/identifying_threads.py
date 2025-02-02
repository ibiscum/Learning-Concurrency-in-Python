import threading
import time


def my_thread():
    print("Thread {} starting".format(threading.currentThread().getName()))
    time.sleep(10)
    print("Thread {} ending".format(threading.currentThread().getName()))


for i in range(4):
    threadName = "Thread-" + str(i)
    thread = threading.Thread(name=threadName, target=my_thread)
    thread.start()

print("{}".format(threading.enumerate()))
