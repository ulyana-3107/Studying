import sys
import signal
import time
# This script only for unix

def handler(signum, frame):
    print(f'Alarm! Job has not done.')
    sys.exit(1)


def job(n):
    data = []
    for x in range(n):
        data.append(x**2)
        time.sleep(0.1)


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(3)
    job(10)
    print('Job 1 done.')
    signal.alarm(0)
    signal.alarm(3)
    job(100)
    print('Job 2 done.')
    signal.alarm(0)
