import random
import time


def slow_function():
    time.sleep(random.randint(1, 5))
    print("Slow Function Executed")


def fast_function():
    print("Fast Function Executed")


def main():
    slow_function()
    fast_function()


if __name__ == '__main__':
    main()
