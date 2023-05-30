# Дан путь к папке (через cmd). Нужно найти и скопировать все файлы с расширением .xml, в котором есть тег
# `<SAVE>...</SAVE>`
# 2. В папку, указанную в значении тега `<SAVE>...</SAVE>` (могут быть разными для каждого файла).


from __future__ import annotations
from pathlib import *
import argparse
from collections import deque
import re
import shutil


def copy_files(src: str | Path, ext: str = '.xml') -> None:
    dst = None
    queue = deque([src])
    pat = r'<SAVE>(.*?)<'

    while queue:
        p = Path(queue.popleft())

        if p.is_file():

            if p.suffix == ext:
                text = p.read_text()

                if '<SAVE>' in text:
                    dst = re.search(pat, text, flags=re.DOTALL).groups()[0]
                    dst = Path(dst)

                    if not dst.exists() or not dst.is_dir():
                        Path(dst).mkdir(parents=True, exist_ok=True)

                    file_name = dst / p.parts[-1]
                    Path(file_name).touch()
                    shutil.copyfile(p, file_name)

        else:
            for elem in p.iterdir():
                queue.append(elem)

    print('Files copied.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to copy files from source to destination folder')
    parser.add_argument('src', type=str, help='path to source folder')
    parser.add_argument('--extension', type=str, default=None, help='file with given extension will be copied')
    args = parser.parse_args()
    copy_files(args.src, args.extension)
