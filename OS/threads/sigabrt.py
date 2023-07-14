import signal
import os


def sigabrt_handler(num, frame):
    print(f'SIGABRT signal got')


signal.signal(signal.SIGABRT, sigabrt_handler)
os.abort()