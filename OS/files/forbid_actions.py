# 3. Дан путь к каталогу (через cmd). Запретить всем пользователям (кроме владельца и группы-владельца)
# менять папку и файлы в ней (только r и x).
import os
import argparse
from main1 import get_numeric_permission
from pathlib import Path
import stat


def set_new_permissions(dir_path: str, permissions: str = '-rwxr-xr-x') -> None:
    np = get_numeric_permission(permissions)
    path = Path(dir_path)

    for file in path.rglob('*'):
        os.chmod(file, eval('0o'+str(np)))

    print('Permissions changed.')


def set_new_permissions2(dir_path: str) -> None:
    path = Path(dir_path)

    for file in path.rglob('*'):
        os.chmod(file, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

    print('Permissions changed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Functions for changing files permissions recursively')
    parser.add_argument('dir_path', type=str, help='Path to the directory')
    parser.add_argument('-p', '--permissions', type=str, default=None)
    args = parser.parse_args()
    if args.permissions is not None:
        set_new_permissions(args.dir_path, args.permissions)
    else:
        set_new_permissions(args.dir_path)