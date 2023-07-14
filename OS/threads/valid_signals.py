import subprocess
import multiprocessing as mp
import os
import time
import random
import sys
import multiprocessing
import signal
# Windows: !SIGABRT, !SIGFPE, !SIGILL, !SIGINT, !SIGSEGV, SIGTERM, !SIGBREAK


def print_valid_signals():
    vs = signal.valid_signals()
    print(f'Number of valid signals on {sys.platform} - {len(vs)}')
    for s in vs:
        print(s, s.name)


if __name__ == '__main__':
    print_valid_signals()