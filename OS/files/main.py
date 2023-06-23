import os
import stat
import re
from collections import deque
from itertools import cycle


def create_if_not_exists(file) -> None:
    if not os.access(file, os.F_OK):
        open(file, 'w').close()


def change_mode(file, mode: str) -> None:
    mode = mode.lower()

    if mode == 'r':
        os.chmod(file, stat.S_IRUSR)
    elif mode == 'w':
        os.chmod(file, stat.S_IWUSR)
    elif mode == 'x':
        os.chmod(file, stat.S_IXUSR)
    elif len(mode.strip()) == 3:
        os.chmod(file, stat.S_IRWXU)


def bin2int(bin: list) -> int:
    num = 0
    for i in range(len(bin)):
        add = bin[i] * 2 ** (len(bin) - 1 - i)
        num += add

    return num


def int2bin(num: int) -> list:
    bin = deque([])

    while num > 0:
        bin.appendleft(num % 2)
        num = num // 2

    return list(bin)


def octal2bin(oct: int) -> list:
    nums = [int(i) for i in str(oct)]
    bin_nums = []

    for num in nums:
        if num > 7:
            raise ValueError('Incorrect data was given')

        bins = int2bin(num)

        if len(bins) < 3:
            bins = [0] * (3 - len(bins)) + bins

        bin_nums.extend(bins)

    return bin_nums


def get_str_permission(num: int) -> str:
    bins = octal2bin(num)
    res, modes = '-', cycle('rwx')
    for b in bins:
        mode = next(modes)
        if b:
            res += mode
        else:
            res += '-'

    return res


def get_numeric_permission(permission: str) -> int:
    pat = r'-[r-][w-][x-][r-][w-][x-][r-][w-][x-]'
    if re.fullmatch(pat, permission) is None:
        raise ValueError('Incorrect data given')

    groups, curr_group = [], ''
    for i in range(len(permission)):
        if i > 0:
            curr_group += permission[i]
            if len(curr_group) == 3:
                groups.append(curr_group)
                curr_group = ''

    for i in range(len(groups)):
        arr = []
        for j in groups[i]:
            if j == '-':
                arr.append(0)
            else:
                arr.append(1)
        groups[i] = arr

    res = ''
    for gr in groups:
        res += str(bin2int(gr))

    return int(res)


if __name__ == '__main__':
    for num in (644, 755, 555, 777):
        print(f'num: {num}, permission: {get_str_permission(num)}')



