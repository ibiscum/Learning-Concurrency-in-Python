""" Learning Concurrency in Python - Chapter 01 - concurrent calculation """

import time
import random
from multiprocessing import Process


def calculate_prime_factors(n):
    """ This does all of our prime factorization on a given number 'n' """
    prime_factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            prime_factors.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors


# We split our workload from one batch of 10,000 calculations
# into 10 batches of 1,000 calculations
def execute_proc():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))


def main():
    print("Starting number crunching")
    t0 = time.time()

    procs = []

    # Here we create our processes and kick them off
    for i in range(10):
        proc = Process(target=execute_proc, args=())
        procs.append(proc)
        proc.start()

    # Again we use the .join() method in order to wait for
    # execution to finish for all of our processes
    for proc in procs:
        proc.join()

    t1 = time.time()
    total_time = t1 - t0
    # we print out the total execution time for our 10
    # procs.
    print("Execution Time: {}".format(total_time))


if __name__ == '__main__':
    main()
