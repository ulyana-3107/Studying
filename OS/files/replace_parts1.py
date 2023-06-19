# Дан файл (параметр cmd). Найти в файле строку [old_part:#number], где #number - длина старой части.
# Нужно (два задания):
# Заменить #number символов от этой конструкции (учитывая её) на #. Важно: никаких temp-файлов создавать нельзя.
# (file.read(size), file.seek(pointer))
#  считаем, что все файлы очень большие и считывать их сразу мы не можем (даже построчно).
#  Максимальный допустимый блок для считывания: 32 байта.


import argparse
import re
from pathlib import Path
import sys
import re


def find_part(text: str) -> int:
    l = len(text) - 1

    while l > -1:
        if text[l] == '[':
            return l
        elif text[l] == ']':
            return 0
        l -= 1

    return 0


def repl_parts(file: str, size: int):
    indx, marks = 0, []
    pat = r'(\[old_part:\s*\d+\s*\])'
    num_pat = r'(\d+)'

    with open(file, 'r', encoding='utf-8-sig') as r:
        sub_text = None
        while True:
            text = r.read(size)

            if sub_text:
                text = sub_text + text

            if text:
                for m in re.finditer(pat, text):
                    txt = text[m.span()[0]: m.span()[1]]
                    num = int(re.findall(num_pat, txt)[0])
                    marks.append([indx, m.span(), num])

                part = find_part(text)

                if part:
                    sub_text = text[part:]
                    indx += part
                    continue

                sub_text = None
                indx += 32

            else:
                break

    file = open(file, 'r+b')

    for elem in marks:
        file.seek(elem[0] + elem[1][0], 0)
        sub_text = '#' * elem[2]
        file.write(sub_text.encode())

    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replaces some parts of a text in a given folder with sign')
    parser.add_argument('file_path', type=str, help='path to the file with text to edit')
    parser.add_argument('byte_size', type=int, help='maximum size of bytes to read at once')
    args = parser.parse_args()
    repl_parts(args.file_path, args.byte_size)