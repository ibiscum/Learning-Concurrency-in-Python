""" Learning Concurrency in Python - Chapter 01 - sequential calculation """

import time
import random


# This does all of our prime factorization on a given number 'n'
def calculate_prime_factors(n_v):
    """ Calculate prime factor. """
    prime_factor = []
    d_v = 2
    while d_v * d_v <= n_v:
        while (n_v % d_v) == 0:
            prime_factor.append(d_v)  # supposing you want multiple factors repeated
            n_v //= d_v
        d_v += 1
    if n_v > 1:
        prime_factor.append(n_v)
    return prime_factor


def main():
    """ Sequential number calculation. """
    print("Starting number crunching")
    t_0 = time.time()

    for _ in range(10000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))

    t_1 = time.time()
    total_time = t_1 - t_0

    print("Execution Time: {}".format(total_time))


if __name__ == '__main__':
    main()
