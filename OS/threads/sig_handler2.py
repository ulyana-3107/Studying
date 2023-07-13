# 2. Написать обработчик для сигнала, получаемого при завершении дочернего процесса, который будет писать
# в консоль что-то вроде "Child process {pid} was finished". Породить n потоков и проверить работу этого
# обработчика.
# 1. Сообщение выводится ещё до того, как что-то завершится...
# 2. В multiprocessing есть доп параметр callback. Попробуй его


import threading
import subprocess
import time
import win32con
import win32event
import multiprocessing
import random
import os


def callback(pid: int):
    print(f'Child process finished with pid: {pid}')


def child_process():
    sl_time = random.randint(1, 5)
    time.sleep(sl_time)
    return os.getpid()


def run_processes(n: int):
    pool = multiprocessing.Pool(processes=n)
    for i in range(n):
        res = pool.apply_async(child_process, callback=callback)

    pool.close()
    pool.join()


if __name__ == "__main__":
    run_processes(5)
