import time
import random


# This does all of our prime factorization on a given number 'n'
def calculate_prime_factors(n):
    prime_factor = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            prime_factor.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        prime_factor.append(n)
    return prime_factor


def main():
    print("Starting number crunching")
    t0 = time.time()

    for i in range(10000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))

    t1 = time.time()
    total_time = t1 - t0

    print("Execution Time: {}".format(total_time))


if __name__ == '__main__':
    main()
