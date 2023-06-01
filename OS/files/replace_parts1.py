# Дан файл (параметр cmd). Найти в файле строку [old_part:#number], где #number - длина старой части.
# Нужно (два задания):
# Заменить #number символов от этой конструкции (учитывая её) на #. Важно: никаких temp-файлов создавать нельзя.
# (file.read(size), file.seek(pointer))


import argparse
import re


def repl_parts(file_name: str) -> None:
    with open(file_name, 'r+', encoding='utf-8-sig') as wr:
        text = wr.read()
        parts, repl_parts = [], []
        pat = r'(\[\w+\s*:\s*\d+\])'
        pat2 = r'(\d+)'

        for it in re.finditer(pat, text):
            num = int(re.findall(pat2, text[it.span()[0]:it.span()[1]])[0])
            parts.append([it.span()[0], num, it.span()[1] - it.span()[0]])

        for part in parts:
            if part[2] > part[1]:
                add_part = text[part[0]: part[0] + part[1] + part[2] - part[1]]
            else:
                add_part = text[part[0]: part[0] + part[1]]
            repl_parts.append([add_part, '#'*len(add_part)])

        for repl in repl_parts:
            text = text.replace(repl[0], repl[1])

        wr.seek(0)
        wr.write(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replaces some parts of a text in a given folder with sign')
    parser.add_argument('file_path', type=str, help='path to the file with text to edit')
    args = parser.parse_args()
    repl_parts(args.file_path)