# 1. Написать скрипт, который будет порождать n потоков. Все дочерние потоки будут спать случайное время
# (от 0 до 10 секунд). Главный поток после порождения потоков ждём 5 секунд и посылает всем своим
# дочерним потокам сигнал SIGTERM. Вернуть число потоков, которые успели завершиться до получения
# этого сигнала


import os
import time
import random
import signal
import subprocess
import argparse


def main(n):
    processes = []
    finished_processes = 0
    for _ in range(n):
        process = subprocess.Popen(['python', 'script.py'], shell=True)
        processes.append(process)

    time.sleep(5)
    # Sending SIGTERM signal to all processes
    for process in processes:
        # process.terminate()
        process.kill()
        if process.poll() is not None:
            finished_processes += 1

    return finished_processes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of processes to run simultaniously')
    args = parser.parse_args()
    res = main(args.N)
    print(f'Number of processes terminated before receiveing a SIGINT - {res}')
