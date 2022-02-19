""" Learning Concurrency in Python - Chapter 01 - concurrent image """

import threading
import urllib.request
import time


def download_image(image_path, file_name):
    """ Download image. """
    print("Downloading Image from ", image_path)
    urllib.request.urlretrieve(image_path, file_name)
    print("Completed Download")


def execute_thread(i):
    """ Execute thread. """
    image_name = "temp/image-" + str(i) + ".jpg"
    download_image("http://lorempixel.com/400/200/sports", image_name)


def main():
    """ Concurrent image download. """
    t_0 = time.time()
    # create an array which will store a reference to
    # all of our threads
    threads = []

    # create 10 threads, append them to our array of threads
    # and start them off
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        threads.append(thread)
        thread.start()

    # ensure that all the threads in our array have completed
    # their execution before we log the total time to complete
    for i in threads:
        i.join()

    # calculate the total execution time
    t_1 = time.time()
    total_time = t_1 - t_0
    print("Total Execution Time {}".format(total_time))


if __name__ == '__main__':
    main()
