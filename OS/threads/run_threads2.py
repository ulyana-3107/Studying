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


def func(res_queue):
    name = inspect.currentframe().f_code.co_name
    print(f'{name} is running...')
    time.sleep(random.randint(1, 10))
    print(f'pid: {os.getpid()}')
    proc_name = current_process().name
    res_queue.put((random.randint(1, 100), proc_name))


def run_threads(n: int) -> dict:
    procs, results = [], {}
    res_queue = Queue()

    for i in range(n):
        process = Process(target=func, args=(res_queue, ))
        procs.append(process)
        process.start()

    while procs:
        chosen = random.choice(procs)
        chosen.join()
        result = res_queue.get()
        results[result[1]] = result[0]
        procs.remove(chosen)

    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of processes to run simultaniously')
    args = parser.parse_args()
    multiprocessing.freeze_support()
    res = run_threads(args.N)
    for pr_name, e_code in res.items():
        print(f'name of process: {pr_name}  exit code: {e_code}')