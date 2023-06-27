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
        if path2 == '':
            return path1

        result_path, sep, c = '', '\\', 0
        spl1, spl2 = deque(path1.split(sep)), deque(path2.split(sep))

        if spl1[-1] == '':
            spl1.pop()
        if spl1[0] == '':
            spl1.popleft()
        if spl2[0] == '':
            spl2.popleft()
        if spl2[-1] == '':
            spl2.pop()

        if len(set(spl1) & set(spl2)):
            if spl1[0] == spl2[0]:
                for i in range(min(len(spl1), len(spl2))):
                    if spl1[i] == spl2[i]:
                        result_path += spl1[i] + sep
                        c += 1
                    else:
                        break

                for i in range(c):
                    spl2.popleft()

                if len(spl2):
                    other_part = sep.join(spl2)

                else:
                    other_part = ''
                result_path += other_part

                return result_path

            else:
                index1, index2 = 0, 0
                for i in range(len(spl1)):
                    if spl1[i] in (set(spl1) & set(spl2)):
                        index1 = i
                        break

                for i in range(len(spl2)):
                    if spl2[i] in (set(spl1) & set(spl2)):
                        index2 = i
                        break

                result_path = sep.join(list(spl1)[: index1]) + sep + sep.join(list(spl2)[index2:])

                return result_path

        else:
            return sep.join(spl1) + sep + sep.join(spl2)

    @staticmethod
    def get_root() -> str:
        return 'C:'

    def get_curr_path(self) -> str:
        return str(os.path.abspath(self.curr_path))

    def cd(self, new_path: str) -> None:
        if new_path.startswith('.'):
            back, parts = 0, new_path.split(self.sep)

            for i in range(len(parts)):
                if parts[i].isalnum():
                    break
                back += 1

            p1 = self.curr_path.split(self.sep)

            if p1[-1] == '':
                p1.pop()

            path1 = self.sep.join(p1[:-back])
            path2 = self.sep.join(parts[back:])
            nwd = self.join(path1, path2)

        else:
            nwd = self.join(self.curr_path, new_path)

        self.curr_path = nwd


wp = Windows('a\\b\\c\\d')
wp.cd('..\\..\\r\\t')
print(wp.curr_path)