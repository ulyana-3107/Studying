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
        if not self.check_path(curr_path):
            raise ValueError('Incorrect path separator!')

        self.curr_path, self.sep = curr_path, '/'

        print('Unix')

    @staticmethod
    def check_path(path: str) -> bool:
        if path.isalnum():
            return True
        if len(path.split('\\')) == 1 or '/' in path or not path.startswith('/'):
            return False
        return True

    @staticmethod
    def join(path1: str, path2: str) -> str:
        if not Unix.check_path(path1) or not Unix.check_path(path2):
            raise ValueError('Incorrect path separator!')

        if path2 == '':
            return path1

        result_path, c, sep = '', 0, '/'
        spl1, spl2 = deque(path1.split(sep)), deque(path2.split(sep))

        if spl1[0] == '':
            spl1.popleft()
        if spl1[-1] == '':
            spl1.pop()
        if spl2[0] == '':
            spl2.popleft()
        if spl2[-1] == '':
            spl2.pop()

        if len(set(spl1) & set(spl2)):
            if spl1[0] == spl2[0]:

                for i in range(min(len(spl1), len(spl2))):
                    if spl1[i] == spl2[i]:
                        c += 1
                        result_path += spl1[i] + sep

                    else:
                        break

                for i in range(c):
                    spl2.popleft()
                if len(spl2):
                    result_path += sep.join(spl2)

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

                return sep.join(list(spl1)[: index1]) + sep + sep.join(list(spl2)[index2:])

        else:
            return sep.join(spl1) + sep + sep.join(spl2)

    @staticmethod
    def get_root() -> str:
        return '/'

    def get_curr_path(self) -> str:
        p = str(Path(self.curr_path).resolve())
        return p.replace('\\', self.sep)

    def cd(self, new_path: str) -> None:
        if not self.check_path(new_path):
            raise ValueError('Incorrect path separator!')

        if new_path.startswith('.'):
            back, parts = 0, new_path.split(self.sep)

            for i in range(len(parts)):
                if parts[i].isalnum():
                    break
                back += 1

            p1 = self.curr_path.split(self.sep)
            path1, path2 = self.sep.join(p1[: -back]), self.sep.join(parts[back:])
            nwd = self.join(path1, path2)

            self.curr_path = nwd

        else:
            nwd = self.join(self.curr_path, new_path)

        self.curr_path = nwd


