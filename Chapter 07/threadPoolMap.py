from concurrent.futures import ThreadPoolExecutor

values = [2, 3, 4, 5, 6, 7, 8]


def multiply_by_two(n):
    return 2 * n


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results_map = executor.map(multiply_by_two, values)
        for result in results_map:
            print(result)


if __name__ == '__main__':
    main()
    results = list(map(multiply_by_two, values))
    print(results)
