from multiprocessing import Process
import time


def my_worker():
    t1 = time.time()
    print("Process started at: {}".format(t1))
    time.sleep(20)


myProcess = Process(target=my_worker)
print("Process {}".format(myProcess))
myProcess.start()
print("Terminating Process...")
myProcess.terminate()
myProcess.join()
print("Process Terminated: {}".format(myProcess))
