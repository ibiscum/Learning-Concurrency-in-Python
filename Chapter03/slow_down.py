import time
import random
import threading


def calculate_prime_factors(n):
    prime_factor = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            prime_factor.append(d)
            n //= d
        d += 1
    if n > 1:
        prime_factor.append(n)
    return prime_factor


def execute_proc():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))


def main():
    print("Starting number crunching")
    t0 = time.time()

    threads = []

    for i in range(10):
        thread = threading.Thread(target=execute_proc)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    t1 = time.time()
    total_time = t1 - t0
    print("Execution Time: {}".format(total_time))


if __name__ == '__main__':
    main()
