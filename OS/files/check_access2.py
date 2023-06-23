import os
import stat
import argparse
from pathlib import Path

# На вход подаётся путь к каталогу (через cmd). Вывести все файлы из этого каталога (на любой глубине),
# которые недоступны для чтения.


def is_readable(file: str | Path) -> bool:
    mode = os.stat(file).st_mode
    fm = stat.filemode(mode)

    return 'r' in fm


def print_not_readable(path: str) -> None:
    print('Non-Readable paths:')
    path = Path(path)

    for name in path.rglob('*'):
        if not is_readable(name):
            print(name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Checking for non-readable files')
    parser.add_argument('dir_path', type=str, help='Path to the folder to iterate')
    args = parser.parse_args()
    print_not_readable(args.dir_path)