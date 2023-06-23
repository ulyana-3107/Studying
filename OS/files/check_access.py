import os
import argparse
import stat


# На вход подаётся список файлов и каталогов (через cmd). Вывести все пути, которые доступны как
# минимум для чтения (r--, rw-, rwx, r-x)


def print_readable_files(*args) -> None:
    print('Readable files:')

    for path in args:
        if os.access(path, os.F_OK) and os.access(path, os.R_OK):
            print(path)


def alternative_way(*args) -> None:
    print('Readable files:')

    for path in args:
        mode = os.stat(path).st_mode
        fm = stat.filemode(mode)
        if 'r' in fm:
            print(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Checking which files are readable')
    parser.add_argument('PATHS', help='Paths to be processed', nargs='*')
    args = parser.parse_args()
    print_readable_files(*args.PATHS)
