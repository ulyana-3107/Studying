import time
import random
import os
import signal
import sys


def sigterm_handler():
    print(f'Process {os.getpid()} got SIGTERM signal')


def run():
    sl = random.randint(1, 10)
    signal.signal(signal.SIGTERM, sigterm_handler)
    time.sleep(sl)
    return os.getpid()


if __name__ == '__main__':
    run()