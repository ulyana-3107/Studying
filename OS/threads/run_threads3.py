# 2. Написать скрипт, который будет порождать n потоков сразу. Далее главный скрипт ждёт пока не завершится любой из
# дочерних потоков и после работает с ним, потом снова ждёт и так далее


import multiprocessing
import os
import sys
import inspect
import time
import random
import argparse
import sys


def func():
    time.sleep(random.randint(1, 10))
    return


def run_threads(num):
    completed_count = 0
    async_results = []
    for _ in range(num):
        pr = multiprocessing.Process(target=func)
        pr.start()
        async_results.append(pr)

    while async_results:
        for i in async_results:
            if not i.is_alive():
                completed_count += 1
                print(f'{completed_count} processes finished.')
                async_results.remove(i)
                break

            time.sleep(1.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of processes to run simultaniously')
    args = parser.parse_args()
    multiprocessing.freeze_support()
    run_threads(args.N)