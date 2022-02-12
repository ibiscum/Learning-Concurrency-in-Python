""" Learning Concurrency in Python - Chapter 01 - sequential image """

import time
import urllib.request


import urllib.request


def download_image(image_path, file_name):
    print("Downloading Image from ", image_path)
    urllib.request.urlretrieve(image_path, file_name)


def main():
    t0 = time.time()
    for i in range(10):
        image_name = "temp/image-" + str(i) + ".jpg"
        download_image("http://lorempixel.com/400/200/sports", image_name)

    t1 = time.time()
    total_time = t1 - t0
    print("Total Execution Time {}".format(total_time))


if __name__ == '__main__':
    main()
