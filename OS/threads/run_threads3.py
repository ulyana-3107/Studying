# 2. Написать скрипт, который будет порождать n потоков сразу. Далее главный скрипт ждёт пока не завершится любой из
# дочерних потоков и после работает с ним, потом снова ждёт и так далее


import multiprocessing
from multiprocessing import current_process
import os
import inspect
import time
import random
import argparse


def func():
    name = inspect.currentframe().f_code.co_name
    print(f'{name} is running...')
    time.sleep(random.randint(1, 10))
    print(f'pid: {os.getpid()}')
    return random.randint(1, 100)


def run_threads(num):
    pool = multiprocessing.Pool()

    async_results = [pool.apply_async(func) for _ in range(num)]

    completed_count = 0
    results = []

    while completed_count < num:
        for async_result in async_results:
            if async_result.ready() and async_result not in results:
                results.append(async_result)
                completed_count += 1

    total_sum = sum([async_result.get() for async_result in results])
    return total_sum


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of processes to run simultaniously')
    args = parser.parse_args()
    multiprocessing.freeze_support()
    res = run_threads(args.N)
    print(f'Sum of returned codes: {res}')
