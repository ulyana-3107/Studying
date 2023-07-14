import sys
import time
import signal


def sigbreak_handler(signum, frame):
    print(f'CTRL_BREAK button was pressed. Terminating...')
    sys.exit()


def run():
    signal.signal(signal.SIGBREAK, sigbreak_handler)
    while 1:
        print(f'Press CTRL-BREAK button.')
        time.sleep(1)


if __name__ == '__main__':
    run()