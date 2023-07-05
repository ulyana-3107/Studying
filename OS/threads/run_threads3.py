# 2. Написать скрипт, который будет порождать n потоков сразу. Далее главный скрипт ждёт пока не завершится любой из
# дочерних потоков и после работает с ним, потом снова ждёт и так далее


import multiprocessing
import os
import inspect
import time
import random
import argparse


def func():
    name = inspect.currentframe().f_code.co_name
    print(f'{name} is running...')
    time.sleep(random.randint(1, 10))
    return random.randint(1, 100), os.getpid()


def run_threads(num):
    pool, completed_count = multiprocessing.Pool(), 0
    async_results = [pool.apply_async(func) for _ in range(num)]

    while completed_count < num:
        chosen = random.choice(async_results)
        while True:
            if chosen.ready():
                completed_count += 1
                async_results.remove(chosen)
                e_code, pid = chosen.get()
                print(f'Process with pid {pid} exited with code {e_code}')
                break

            time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of processes to run simultaniously')
    args = parser.parse_args()
    multiprocessing.freeze_support()
    run_threads(args.N)