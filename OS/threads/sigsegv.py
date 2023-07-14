import signal
import ctypes


def sigsegv_handler(signum, frame):
    print(f'signal SIGSEGV got.')


if __name__ == '__main__':
    signal.signal(signal.SIGSEGV, sigsegv_handler)
    ctypes.string_at(0)