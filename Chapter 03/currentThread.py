import threading
import time


def my_child_thread():
    print("Child Thread Starting")
    time.sleep(5)
    print("Current Thread ----------")
    print(threading.current_thread())
    print("-------------------------")
    print("Main Thread -------------")
    print(threading.main_thread())
    print("-------------------------")
    print("Child Thread Ending")


child = threading.Thread(target=my_child_thread)
child.start()
child.join()
