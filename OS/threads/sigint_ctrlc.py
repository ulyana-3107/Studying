import sys
import signal
import time


def sigint_handler(signum, frame):
    print(f'CTRL-C button was pressed. Terminating...')
    sys.exit(0)


def run1():
    signal.signal(signal.SIGINT, sigint_handler)
    while 1:
        print('lol')
        time.sleep(2)


if __name__ == '__main__':
    run1()