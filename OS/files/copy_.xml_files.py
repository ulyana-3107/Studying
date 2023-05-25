# 3. Дан путь к папке (через cmd). Нужно найти и скопировать все файлы с расширением .xml, в котором есть тег
# `<SAVE>...</SAVE>`:
#    1. В папку, переданную через cmd (--output).


from pathlib import *
import argparse
from collections import deque
import shutil


def copy_files(src: str | Path, dst: str | Path, ext: str = '.xml') -> None:
    if not Path(dst).exists():
        Path.mkdir(dst)

    queue = deque([src])

    while queue:
        p = queue.popleft()
        if Path(p).is_file():

            if Path(p).suffix == ext:

                text = Path(p).read_text()

                if '<save>' in text or '<save>'.upper() in text:
                    new = dst + '\\' + Path(p).stem + ext
                    Path(new).touch()
                    shutil.copyfile(Path(p), new)

        else:
            for elem in Path(p).iterdir():
                queue.append(elem)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File with script that copies files from src directory to dst')
    parser.add_argument('src_path', type=str, help='path to a source directory')
    parser.add_argument('dst_path', type=str, help='path where files should be copied')
    parser.add_argument('-ext', '--extension', type=str, default=None,
                        help='files with given extension only should be copied, (default=None)')
    arguments = parser.parse_args()

    copy_files(arguments.src_path, arguments.dst_path, arguments.extension)