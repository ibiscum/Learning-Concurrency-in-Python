import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

values = [2, 3, 4, 5, 6, 7, 8]


def multiply_by_two(n):
    return 2 * n


def done():
    print("Task Done")


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(multiply_by_two, values)

        for result in results:
            print(result)


if __name__ == '__main__':
    main()
