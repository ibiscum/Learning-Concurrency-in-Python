import threading
import time


def my_thread(_my_event):
    while not _my_event.is_set():
        print("Waiting for Event to be set")
        time.sleep(1)
    print("myEvent has been set")


def main():
    my_event = threading.Event()
    thread1 = threading.Thread(target=my_thread, args=(my_event,))
    thread1.start()

    time.sleep(10)
    my_event.set()


if __name__ == '__main__':
    main()
