# 2. Работа с путями и cmd: на вход (через cmd) подаются произвольное количество путей. Нужно для каждого из них:
#
#    1. Проверить, настоящий ли это путь (существует ли объект).
#    2. Если существует, то что это? Папка, файл, ссылка?
#    3. Если файл, то какое у него расширение?
#    4. Если папка, то сколько внутри неё объектов? (Отдельно число файлов и число папок, файлы во вложенных папках тоже
#    учитываем)
#    5. Сколько весит? (Если ссылка, то сколько весит объект, на который она указывает. Для папки считаем сумму весов
#    всех файлов)
#    6. Узнать абсолютный путь.
#    7. Если через cmd дополнительно передан необязательный параметр --root-path, то найти относительный путь
#    от --root-path.


import argparse
import os
from pathlib import Path
from collections import deque


def procedure_count_objects_and_calc_weight(path: str) -> None:
    """
    This procedure displays the number of objects (using bfs) found along this path, specifying the details
    """
    dirs, files, total_weight = 0, 0, 0
    queue = deque([path])
    while queue:
        p = queue.popleft()

        for elem in os.listdir(p):
            if elem == '__pycache__':
                continue

            name = p + '\\' + elem

            if os.path.isdir(name):
                queue.append(name)
                dirs += 1
            elif os.path.isfile(name):
                files += 1
                total_weight += Path(name).stat().st_size

    print(f'objects found total: {files + dirs}\nfiles found: '
          f'{files}\ndirectories found: {dirs}\ntotal weight: {total_weight}')


def give_info_about_paths(root_path: str = None, *paths) -> None:
    for path in paths:
        print(f'Path name: {path}')

        if not Path(path).exists():
            print('Not exists\n')
            continue

        print('Info:')

        is_file, is_dir, is_symlink = Path(path).is_file(), Path(path).is_dir(), Path(path).is_symlink()
        file_type = 'file' if is_file else 'directory' if is_dir else 'symbolic link'
        print(f'file type: {file_type}')

        if is_file:
            file_ext = Path(path).suffix
            print(f'file extension: {file_ext}')
            print(f'weight of file: {Path(path).stat().st_size}')

        elif is_dir:
            procedure_count_objects_and_calc_weight(path)

        else:
            print('here must be weight of a object that link points to')

        print(f'absolute path: {Path(path).resolve()}')
        if root_path:
            try:
                rel_path = Path(path).relative_to(Path(root_path))
                print(f'Path, relative to {root_path}: {rel_path}')
            except ValueError:
                print(f'{path} is not relative to {root_path}')
        print('-'*65, '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Function/s to process given paths')
    parser.add_argument('PATHS', help='paths to be processed', nargs='*')
    parser.add_argument('-rp', '--root_path', type=str, default=None,
                        help='root path to find relative path (default=None)')
    arguments = parser.parse_args()
    give_info_about_paths(arguments.root_path, *arguments.PATHS)

