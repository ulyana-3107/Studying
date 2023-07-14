import signal


def sigfpe_handler(signum, frame):
    print(f'SIGFPE signal got.')


if __name__ == '__main__':
    signal.signal(signal.SIGFPE, sigfpe_handler)
    print(1/0)