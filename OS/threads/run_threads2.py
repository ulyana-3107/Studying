# 2. Написать скрипт, который будет порождать n потоков сразу. Далее главный скрипт случайно выбирает
# потомка и ждёт завершение именно его, запоминает его код возврата, выбирает другого случайного
# потомка и ждёт его и так далее. Потомок делает ту же работу, что и в задании 1.
import multiprocessing
from multiprocessing import Process, current_process, Queue
import os
import inspect
import random
import time
import argparse
import sys


def func():
    time.sleep(random.randint(1, 10))
    print(f'pid: {os.getpid()}')
    sys.exit(random.randint(1, 100))


def run_threads(n: int):
    procs = []

    for i in range(n):
        process = Process(target=func)
        procs.append(process)
        process.start()

    while procs:
        chosen = random.choice(procs)
        chosen.join()
        name = chosen.name
        ex_code = chosen.exitcode
        print(f'{name} exited with code {ex_code}')
        procs.remove(chosen)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of processes to run simultaniously')
    args = parser.parse_args()
    multiprocessing.freeze_support()
    run_threads(args.N)
