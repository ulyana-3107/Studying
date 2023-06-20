# 4. Дан путь к html-файлу (через cmd) и путь к папке для вывода (--output). Необходимо скопировать данный файл и все
# файлы, на который он ссылается (картинки, другие html-файлы). **Важно: Если есть ссылка на другой html-файл, то
# проверить наличие ссылок и в нём. **


from pathlib import *
import argparse
from collections import deque
import re
import shutil


def make_full_path(elem: str, base_path: str) -> Path:
    indx = 0

    while indx < len(elem) - 1:
        if elem[indx].isalnum():
            break

        indx += 1

    steps_back = elem[:indx].count('.')//2 + 1
    parts = Path(base_path).parts[: -steps_back]

    return Path('\\'.join(parts) + '\\' + elem[indx:])


def copy_files(src: str | Path, dst: str | Path) -> None:
    queue, db = deque([src]), set()
    pat = r'href=[\'"](.*?)[\'"]'
    pat2 = r'<img src\s?=\s?[\'"](.+?)[\'"]'
    base_path = Path(src).parent

    if not Path(dst).exists or not Path(dst).is_dir():
        Path(dst).mkdir()

    file = dst + '\\' + str(Path(src).parts[-1])
    if not Path(file).exists():
        shutil.copy2(src, dst)
        db.add(Path(src))

    while queue:
        p = Path(queue.popleft())
        text = p.read_text()
        links, img_links = re.findall(pat, text), re.findall(pat2, text)
        links.extend(img_links)

        for elem in links:
            path = Path(elem)
            if not elem.startswith('.'):
                full = base_path.joinpath(path)
            else:
                full = make_full_path(elem, str(p))

            if full.exists() and full not in db:
                if '.html' in elem:
                    queue.append(str(full))

                f_name = dst + '\\' + str(Path(elem).parts[-1])
                if not Path(f_name).exists():
                    Path(f_name).touch()
                    shutil.copyfile(full, f_name)

                db.add(full)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Working with html file')
    parser.add_argument('src_path', type=str, help='path to the html file')
    parser.add_argument('dst_path', type=str, help='path for extracting files there')
    args = parser.parse_args()
    copy_files(args.src_path, args.dst_path)