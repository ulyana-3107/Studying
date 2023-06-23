import os
import stat


def create_if_not_exists(file) -> None:
    if not os.access(file, os.F_OK):
        open(file, 'w').close()


def change_mode(file, mode: str) -> None:
    mode = mode.lower()

    if mode == 'r':
        os.chmod(file, stat.S_IRUSR)
    elif mode == 'w':
        os.chmod(file, stat.S_IWUSR)
    elif mode == 'x':
        os.chmod(file, stat.S_IXUSR)
    elif len(mode.strip()) == 3:
        os.chmod(file, stat.S_IRWXU)


f1 = 'created_file.py'
f2 = 'number2.txt'
f3 = 'this_is_file3.txt'

p = r'C:\Users\andre\PycharmProjects\Studying\OS\files\test\created_file.py'
os.chmod(p, stat.S_IRUSR)