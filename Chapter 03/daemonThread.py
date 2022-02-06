import threading
import time


def standard_thread():
    print("Starting my Standard Thread")
    time.sleep(20)
    print("Ending my standard thread")


def daemon_thread():
    while True:
        print("Sending Out Heartbeat Signal")
        time.sleep(2)


if __name__ == '__main__':
    standardThread = threading.Thread(target=standard_thread)
    daemonThread = threading.Thread(target=daemon_thread)
    daemonThread.setDaemon(True)
    daemonThread.start()

    standardThread.start()
