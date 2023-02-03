import re


text = '''PATH=C:\\Windows\\system32;DinamicProg;C:\\Windows;Algorithms;C:\\Windows\\System32\\Wbem;Addition;
C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;RegEx;C:\Windows\\System32\\OpenSSH\;LC/n_433.py;C:\\Program Files\\
Git\\cmd;Recursion;C:\\Users\\ulyana\\AppData\\Local\\Microsoft\\WindowsApps;'''


def local_files(text: str) -> list:
    paths = re.split(';', text)
    return [p for p in paths if p.startswith('C:')]


print(local_files(text))

