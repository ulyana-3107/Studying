import sys
import signal
import time
import ctypes
import subprocess


def sigill_handler(num, frame):
    print(f'SIGILL signal got.')


signal.signal(signal.SIGILL, sigill_handler)
subprocess.run(['python', 'file'])