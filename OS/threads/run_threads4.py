# 4. Написать программу, которая будет порождать потомка, который будет порождать потомка и так далее
# (всего будет порождено n потомков). Каждый потомок будет ждать завершение порождённого (кроме
# последнее) и спать случайное время (от 1 до 10 секунд), а после завершаться с кодом возврата = код
# возврата ожидаемого потока (0 для последнего) + случайное число (от 1 до 100)


import multiprocessing
import random
import time
import argparse


def child_thread(n: int):
    if n == 0:
        return 0 + random.randint(1, 100)
    else:
        print('child process is running...')
        time.sleep(random.randint(1, 10))
        return random.randint(1, 100) + child_thread(n - 1)


def run_threads(n: int):
    return child_thread(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of processes to run')
    args = parser.parse_args()
    codes = run_threads(args.N)
    print(f'Sum of all codes: {codes}')