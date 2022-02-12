import threading
import time


class MyWorker:

    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock()

    def modify_a(self):
        with self.rlock:
            print("Modifying A : RLock Acquired: {}".format(self.rlock._is_owned()))
            print("{}".format(self.rlock))
            self.a = self.a + 1
            time.sleep(5)

    def modify_b(self):
        with self.rlock:
            print("Modifying B : RLock Acquired: {}".format(self.rlock._is_owned()))
            print("{}".format(self.rlock))
            self.b = self.b - 1
            time.sleep(5)

    def modify_a_b(self):
        with self.rlock:
            print("Rlock acquired, modifying A and B")
            print("{}".format(self.rlock))
            self.modify_a()
            print("{}".format(self.rlock))
            self.modify_b()
        print("{}".format(self.rlock))


worker_a = MyWorker()
worker_a.modify_a_b()
