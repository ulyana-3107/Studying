import signal
import time
import sys
import os
import datetime
# This script only for Unix


def handle(signum, frame):
    print(f'{0} - Signal arrived'.format(datetime.datetime.now()))


def job(n):

    for x in range(n):
        print(os.getpid())
        if x == 5:
            signal.pause()

        print(f'{0} - value = {1}'.format(datetime.datetime.now(), x**2))
        time.sleep(0.5)


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handle)
    job(10)