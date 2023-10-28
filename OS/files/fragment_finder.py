import os
import re
from typing import Union
import imghdr


def search_(data: str, path: str, string, reg, str_arr, reg_arr) -> None:
    if string and data.find(string) != -1:
        print(f'String "{string}" found in {path}')

    if reg:
        m = re.search(reg, data)
        if m:
            print(f'Regular expression {reg} found in {path}')

    for s in str_arr:
        if data.find(s) != -1:
            print(f'String "{s}" found in {path}')

    for reg in reg_arr:
        m = re.search(reg, data)
        if m:
            print(f'Regular expression {reg} found in {path}')


def search(folder, string: Union[str, None], reg: Union[str, None], str_arr: list = [], reg_arr: list = []) -> None:
    for elem in os.listdir(folder):
        path = os.path.join(folder, elem)
        if os.path.isdir(path):
            search(path, string, reg, str_arr, reg_arr)

        elif os.path.isfile(path):
            # if imghdr.what(path) is not None:
            #     continue
            try:
                with open(path, 'r', encoding='utf-8-sig') as reader:
                    data = reader.read()
                search_(data, path, string, reg, str_arr, reg_arr)
            except:
                continue
        else:
            raise FileNotFoundError(f'{path} is not a file or directory')