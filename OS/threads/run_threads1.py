# 1. Написать скрипт, который будет порождать n потоков последовательно: создает поток и ждёт, пока он
# окончится, потом создаёт другой и так далее. Что делает дочерний поток: пишет свой PID, спит рандомное
# время (от 1 до 10 секунд) и завершается со случайным кодом возврата (от 1 до 100). Главный поток должен
# вернуть сумму кодов возврата.
# 1. Сделать через os.fork() # Если работает на Windows
# 2. Сделать через mulprocessing/что-то другое


import threading
import multiprocessing
import time
import random
import inspect
import os
import argparse


def func():
    name = inspect.currentframe().f_code.co_name
    print(f'{name} is running...')
    time.sleep(random.randint(1, 10))
    print(f'pid: {os.getpid()}')


def start_processes(n: int) -> int:
    sum_of_codes = 0

    for i in range(n):
        process = multiprocessing.Process(target=func)
        process.start()
        process.join()
        if process.exitcode == 0:
            sum_of_codes + random.randint(1, 100)

    return sum_of_codes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='script for running processes')
    parser.add_argument('N', type=int, help='Number of processes to run!')
    args = parser.parse_args()
    exit_codes = start_processes(args.N)
    print(f'Sum of random exit codes of all processes: {exit_codes}')

