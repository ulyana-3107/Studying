# 4. Написать программу, которая будет порождать потомка, который будет порождать потомка и так далее
# (всего будет порождено n потомков). Каждый потомок будет ждать завершение порождённого (кроме
# последнее) и спать случайное время (от 1 до 10 секунд), а после завершаться с кодом возврата = код
# возврата ожидаемого потока (0 для последнего) + случайное число (от 1 до 100)


import multiprocessing
import random
import time
import sys
import argparse


def child_thread(n: int):
    if n == 0:
        time.sleep(random.randint(1, 10))
        sys.exit(random.randint(1, 100))
    else:
        time.sleep(random.randint(1, 10))
        child = multiprocessing.Process(target=child_thread, args=(n-1, ))
        child.start()
        child.join()
        sys.exit(child.exitcode + random.randint(1, 100))


def run_threads(n: int):
    pr = multiprocessing.Process(target=child_thread, args=(n, ))
    pr.start()
    pr.join()
    return pr.exitcode


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of processes to run')
    args = parser.parse_args()
    codes = run_threads(args.N)
    print(f'Sum of all codes: {codes}')