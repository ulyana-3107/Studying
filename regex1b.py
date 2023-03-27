import re


def local_paths(text: str) -> list:
    pat = r'[A-Z]:(?:[\|\\][A-Za-zа-яА-Я0-9._\s]+[\|\\]?)+;'
    return re.findall(pat, text, flags=re.MULTILINE)


text = '''PATH=C:\\Windows\\system32;
DinamicProg;
C:\\Windows;
Algorithms;
C:\\Windows\\System32\\Wbem;
D:\\Windows\\system32;
Addition;
C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;
RegEx;
C:\Windows\\System32\\OpenSSH\;
LC/n_433.py;
C:\\Program Files\\Git\\cmd;
Recursion\\solutions;
C:\\Users\\ulyana\\AppData\\Local\\Microsoft\\WindowsApps;'''


with open('paths_input_1b.txt', 'w', encoding='utf-8-sig') as paths_writer:
    paths_writer.write(text)

with open('paths_input_1b.txt', 'r', encoding='utf-8-sig') as paths_reader:
    paths = ''
    for l in paths_reader.readlines():
        paths += l
    print(paths)
    local_paths = local_paths(paths)
    print(local_paths)

with open('local_paths_1b.txt', 'w', encoding='utf-8-sig') as paths_writer:
    for path in local_paths:
        paths_writer.write(path+'\n')


