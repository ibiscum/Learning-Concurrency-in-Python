import threading
import time


class Parent(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.process = None

    def run(self):
        for i in range(10):
            child_thread = threading.Thread(target=self.child)
            child_thread.start()

    def kill(self):
        print("Trying to kill thread")
        if self.process is not None:
            self.process.terminate()
            self.process = None

    @staticmethod
    def child():
        print("{} starting".format(threading.currentThread().getName()))
        time.sleep(10)
        print("{} ending".format(threading.currentThread().getName()))


parent = Parent()
parent.start()
time.sleep(2)
parent.kill()
