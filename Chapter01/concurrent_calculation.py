""" Learning Concurrency in Python - Chapter 01 - concurrent calculation """

import time
import random
from multiprocessing import Process


def calculate_prime_factors(n_p):
    """ This does all of our prime factorization on a given number 'n' """
    prime_factors = []
    d_v = 2
    while d_v * d_v <= n_p:
        while (n_p % d_v) == 0:
            prime_factors.append(d_v)  # supposing you want multiple factors repeated
            n_p //= d_v
        d_v += 1
    if n_p > 1:
        prime_factors.append(n_p)
    return prime_factors


def execute_proc():
    """ We split our workload from one batch of 10,000 calculations into 10 batches of 1,000
    calculations """
    for _ in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))


def main():
    """ Concurrent calculation """
    print("Starting number crunching")
    t_0 = time.time()

    procs = []

    # Here we create our processes and kick them off
    for _ in range(10):
        proc = Process(target=execute_proc, args=())
        procs.append(proc)
        proc.start()

    # Again we use the .join() method in order to wait for
    # execution to finish for all of our processes
    for proc in procs:
        proc.join()

    t_1 = time.time()
    total_time = t_1 - t_0

    # we print out the total execution time for our 10 procs.
    print(f"Execution Time: {total_time}")


if __name__ == '__main__':
    main()
