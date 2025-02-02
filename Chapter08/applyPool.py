from multiprocessing import Pool
import time


def my_task(n):
    time.sleep(n / 2)
    return n * 2


def my_callback(result):
    print("hi")
    print(result)


def main():
    print("apply_async")
    with Pool(4) as p:
        task1 = p.apply_async(func=my_task, args=(4,))
        task2 = p.apply_async(func=my_task, args=(3,))
        task3 = p.apply_async(func=my_task, args=(2,))
        task4 = p.apply_async(func=my_task, args=(1,))

        print(task1.get())
        print(task2.get())
        print(task3.get())
        print(task4.get())


if __name__ == '__main__':
    main()
