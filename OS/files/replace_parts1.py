# Дан файл (параметр cmd). Найти в файле строку [old_part:#number], где #number - длина старой части.
# Нужно (два задания):
# Заменить #number символов от этой конструкции (учитывая её) на #. Важно: никаких temp-файлов создавать нельзя.
# (file.read(size), file.seek(pointer))
#  считаем, что все файлы очень большие и считывать их сразу мы не можем (даже построчно).
#  Максимальный допустимый блок для считывания: 32 байта.


import argparse
import re
from pathlib import Path


def repl_parts(file_name: str, b_size: int = 32) -> None:
    f_name2 = 'edited_' + str(Path(file_name).parts[-1])
    pat = r'(\[old_part\s*:\s*\d+\s*\])'
    pat2 = r'(\d+)'
    rest = ''

    with open(file_name, 'rb') as reader:
        with open(f_name2, 'w', encoding='utf-8-sig') as writer:
            while True:
                parts, repl_parts = [], []
                sub_text = reader.read(b_size)

                if sub_text:
                    sub_text = rest + str(sub_text, 'utf-8-sig')
                    rest = ''
                    closed = False
                    end, i = len(sub_text) // 2, len(sub_text) - 1

                    while i > end:
                        if sub_text[i] == '[':

                            if closed:
                                break

                            index = - (len(sub_text) - abs(i))
                            rest = sub_text[index:]
                            sub_text = sub_text[: index]
                            break

                        elif sub_text[i] == ']':
                            closed = True

                        i -= 1

                    for it in re.finditer(pat, sub_text):
                        num = int(re.findall(pat2, sub_text[it.span()[0]: it.span()[1]])[0])
                        parts.append([it.span()[0], sub_text[it.span()[0]: it.span()[1]], num])

                    for p in parts:
                        start, elem, num = p

                        if num > len(elem):
                            sub_part = elem + sub_text[start + len(elem): start + num]

                        else:
                            sub_part = sub_text[start: start + num]

                        repl_parts.append([sub_part, '#' * len(sub_part)])

                    for repl in repl_parts:
                        sub_text = sub_text.replace(repl[0], repl[1])

                    writer.write(sub_text)

                else:
                    break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replaces some parts of a text in a given folder with sign')
    parser.add_argument('file_path', type=str, help='path to the file with text to edit')
    parser.add_argument('byte_size', type=int, help='maximum size of bytes to read at once')
    args = parser.parse_args()
    repl_parts(args.file_path, args.byte_size)