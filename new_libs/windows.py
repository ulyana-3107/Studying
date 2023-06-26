#  Написать две библиотечки-файла (widnows.py, unix.py), где лежит класс (Windows/Unix)PathHandler и
# методами:
# Статические: join(path_1: str, path_2: str) -> str get_root() -> srt ("C:" для Windows, "/" для Unix)
# Обычные: _init_(self, curr_path) - Выводит сообщение "Windows" или "Unix" и определяет поле curr_path
# cd(new_path: str) - Путь может быть относительным
# get_curr_path() -> str - Абсолютный текущий путь (Можно использовать os.abspath())
# Обеспечить постоянную проверку на правильность формы путей (\ у Windows, / у Unix). Существование
# путей проверять не нужно.
import re
from collections import deque
import os


class Windows:
    def __init__(self, curr_path: str):
        self.sep = '\\'
        self.curr_path = curr_path
        print('Windows')

    @staticmethod
    def join(path1: str, path2: str) -> str:
        result_path, sep, c = '', '\\', 0
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
        return 'C:'

    def get_curr_path(self) -> str:
        return str(os.path.abspath(self.curr_path))

    def cd(self, new_path: str) -> None:
        sep, nwd, c = '\\', '', 0
        spl1, spl2 = self.curr_path.split(sep), deque(new_path.split(sep))

        if new_path.startswith('.'):
            parts = new_path.split(self.sep)
            back = 0
            for p in parts:
                if p.startswith('.'):
                    back += 1

            if back > len(spl1):
                raise ValueError('Incorrect path given')
            for i in range(back):
                spl1.pop()
                spl2.popleft()

        if not len(spl2):
            nwd += sep.join(spl1)
        else:
            for i in range(min(len(spl1), len(spl2))):
                if spl1[i] == spl2[i]:
                    nwd += spl1[i] + sep
                    c += 1
                else:
                    break

            for j in range(c):
                spl2.popleft()

        if nwd:
            nwd += sep.join(spl2)
        else:
            nwd += sep.join(spl1) + sep.join(spl2)

        self.curr_path = nwd