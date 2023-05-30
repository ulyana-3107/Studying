# 4. Дан путь к html-файлу (через cmd) и путь к папке для вывода (--output). Необходимо скопировать данный файл и все
# файлы, на который он ссылается (картинки, другие html-файлы). **Важно: Если есть ссылка на другой html-файл, то
# проверить наличие ссылок и в нём. **


from pathlib import *
import argparse
from collections import deque
import re
import shutil


def copy_files(src: str | Path, dst: str | Path) -> None:
    queue = deque([src])
    pat = r'href=[\'"](.*?)[\'"]'
    pat2 = r'<img src\s?=\s?[\'"](.+?)[\'"]'
    db = set()

    while queue:
        p = Path(queue.popleft())
        text = p.read_text()
        links = re.findall(pat, text)
        img_links = re.findall(pat2, text)
        links.extend(img_links)

        for elem in links:
            path = Path(elem)
            full = path.resolve()

            if full.exists():
                if '.html' in elem and elem not in db:
                    queue.append(elem)
                    db.add(elem)

                f_name = dst + '\\' + path.parts[-1]
                Path(f_name).touch()
                shutil.copyfile(full, f_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Working with html file')
    parser.add_argument('src_path', type=str, help='path to the html file')
    parser.add_argument('dst_path', type=str, help='path for extracting files there')
    args = parser.parse_args()
    copy_files(args.src_path, args.dst_path)
