# Дан ещё один файл (через cmd --new-parts), где в каждой строке лежит замена для старых частей.
# Произвести замену ими. Создавать temp-файл можно.


import argparse
from pathlib import Path
import re
from collections import deque


def repl_parts(src_file_path: str, repl_parts_path: str, b_size: int = 32) -> None:
    f_name = 'edited_2' + str(Path(src_file_path).parts[-1])
    rest = ''
    pat = r'(\[old_part\s*:\s*\d+\s*\])'
    pat2 = r'(\d+)'

    with open(src_file_path, 'rb') as reader1:
        with open(repl_parts_path, 'r', encoding='utf-8-sig') as reader2:
            with open(f_name, 'w', encoding='utf-8-sig') as writer:
                while True:
                    parts, repl_parts = [], []
                    sub_text = reader1.read(b_size)
                    if sub_text:
                        sub_text = rest + str(sub_text, 'utf-8-sig')
                        closed, end, i, rest = False, len(sub_text)//2, len(sub_text) - 1, ''
                        while i > end:
                            if sub_text[i] == '[':
                                if closed:
                                    break
                                index = -(len(sub_text) - i)
                                rest = sub_text[index: ]
                                sub_text = sub_text[: index]
                                break
                            elif sub_text[i] == ']':
                                closed = True
                            i -= 1

                        for it in re.finditer(pat, sub_text):
                            sp = it.span()
                            num = int(re.findall(pat2, sub_text[sp[0]: sp[1]])[0])
                            parts.append([sp[0], num])

                        for p in parts:
                            repl = reader2.readline()
                            r_part = sub_text[p[0]: p[0] + p[1]]
                            repl_parts.append([r_part, repl])

                        for repl in repl_parts:
                            sub_text = sub_text.replace(repl[0], repl[1])

                        writer.write(sub_text)

                    else:
                        break


def split_parts(file: str) -> list:
    text = Path(file).read_text()
    return text.split('\n')


def find_part(txt: str) -> int:
    l = len(txt) - 1
    while l > -1:
        if txt[l] == ']':
            return 0
        elif txt[l] == '[':
            return l
        l -= 1
    return 0


def repl_parts2(src_file: str, parts_file: str, b_size: int = 32) -> None:
    parts = deque(split_parts(parts_file))
    indx, marks = 0, []
    pat, num_pat = r'(\[\s*old_part\s*:\s*\d+\s*\])', r'\d+'

    with open(src_file, 'r', encoding='utf-8-sig') as reader:
        sub_text = None

        while True:
            text = reader.read(b_size)
            if sub_text:
                text = sub_text + text

            if text:
                for m in re.finditer(pat, text):
                    marks.append([indx, m.span(), parts.popleft()])

                part = find_part(text)
                if part:
                    sub_text = text[part:]
                    indx += part
                    continue

                sub_text = None
                indx += b_size

            else: break

    file = open(src_file, 'r+b')

    for mark in marks:
        sub_text = mark[2]

        if len(sub_text) < mark[1][1] - mark[1][0]:
            rest = mark[1][1] - mark[1][0] - len(sub_text)
            sub_text += ' ' * rest

        file.seek(mark[0] + mark[1][0], 0)
        file.write(sub_text.encode())

    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replaces some parts with given parts')
    parser.add_argument('file_path', type=str, help='path to a source file')
    parser.add_argument('parts_file_path', type=str, help='path to the file with parts to replace with')
    parser.add_argument('byte_size', type=int, help='maximum part size in bytes to read file')
    args = parser.parse_args()

    repl_parts2(args.file_path, args.parts_file_path, args.byte_size)