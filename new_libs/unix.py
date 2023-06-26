#  Написать две библиотечки-файла (widnows.py, unix.py), где лежит класс (Windows/Unix)PathHandler и
# методами:
# Статические: join(path_1: str, path_2: str) -> str get_root() -> srt ("C:" для Windows, "/" для Unix)
# Обычные: _init_(self, curr_path) - Выводит сообщение "Windows" или "Unix" и определяет поле curr_path
# cd(new_path: str) - Путь может быть относительным
# get_curr_path() -> str - Абсолютный текущий путь (Можно использовать os.abspath())
# Обеспечить постоянную проверку на правильность формы путей (\ у Windows, / у Unix). Существование
# путей проверять не нужно.
from collections import deque
import os
from pathlib import Path


class Unix:

    def __init__(self, curr_path: str):
        self.curr_path = curr_path
        self.sep = '/'
        print('Unix')

    @staticmethod
    def join(path1: str, path2: str) -> str:
        result_path, sep, c = '', '/', 0
        spl1, spl2 = deque(path1.split(sep)), deque(path2.split(sep))
        if spl1[-1] == '':
            spl1.pop()
        if spl1[0] == '':
            spl1.popleft()
        if spl2[0] == '':
            spl2.popleft()
        for i in range(min(len(spl1), len(spl2))):
            if spl1[i] == spl2[i]:
                result_path += spl1[i] + sep
                c += 1
            else:
                break
        for j in range(c):
            spl2.popleft()

        if result_path != '':
            result_path += sep.join(spl2)
        else:
            result_path += sep.join(spl1) + sep + sep.join(spl2)

        return result_path

    @staticmethod
    def get_root() -> str:
        return '/'

    def get_curr_path(self) -> str:
        p = str(Path(self.curr_path).resolve())
        return p.replace('\\', self.sep)

    def cd(self, new_path: str) -> None:
        self.curr_path = self.join(self.curr_path, new_path)



