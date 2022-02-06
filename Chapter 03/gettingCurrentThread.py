import threading


def thread_target():
    print("Current Thread: {}".format(threading.current_thread()))


threads = []

for i in range(10):
    thread = threading.Thread(target=thread_target)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
