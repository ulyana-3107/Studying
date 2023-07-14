# 3. Написать программу, которая будет порождать поток, который будет порождать поток и так далее.
# Последний поток засыпает на 30 минут, остальные (кроме главного) ждут окончание своего дочернего
# потока. Главный поток посылает своему дочернему сигнал SIGTERM. Написать обработчик для этого
# сигнала, чтобы все потоки сначала посылали SIGTERM своим дочерним потокам, ждали 60 секунд и
# убивали их (если он так и не завершился) и корректно возвращались.


import threading
import time
import signal
import os
import sys
import argparse


def child_thread(i, n):

    print(f'thread {i}: starting...')
    if i < n - 1:
        t = threading.Thread(target=child_thread, args=(i + 1, n))
        t.start()
        print(f'thread {i}: waiting for thread {i + 1} to finish')
        t.join()
    else:
        print(f'thread {i}: sleeping for 30 minutes')
        time.sleep(30 * 60)

    print(f'thread {i}: exiting...')


def sigterm_handler():
    print('received SIGTERM')

    time.sleep(60)

    for thread in threading.enumerate():
        if thread != threading.main_thread():
            thread._stop()

    print('Main Thread: Exiting...')
    sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='Number of threads to start recursively')
    args = parser.parse_args()
    t = threading.Thread(target=child_thread, args=(0, args.n))
    signal.signal(signal.SIGTERM, sigterm_handler)
    t.start()
    time.sleep(5)

    for th in threading.enumerate():
        if th != threading.main_thread():
            th.join(timeout=0)

    print('All threads have exited.')
