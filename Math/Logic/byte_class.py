# Создать класс с одним полем flags типа int (считаем, что он не более 1 байта [-128, 127]). Реализовать методы для
# работы со значениями флагов (всего 8 штук - 1 бит = 1 флаг). Что-то вроде функции get_flag(position: int) -> boolean,
# set_flag(position: int, val: boolean).
from collections import deque
# 1. self.flags должно быть типа int, а не list. Так ты ничего не экономишь по памяти
# (у тебя по сути будет занимать n*sizeof(int) памяти для всех boolean, а достаточно только одного int)


class Byte:
    min_pos, max_pos = 0, 7

    @classmethod
    def position_validate(cls, pos) -> bool:
        return cls.min_pos <= pos <= cls.max_pos

    def __init__(self, flags: int = 0):
        self.flags = flags

    def bin2int(self, bin: list | deque) -> int:
        num = 0
        for i in range(len(bin) - 1, -1, -1):
            num += bin[i] * 2 ** (len(bin) - i - 1)

        return num

    def int2bin(self, num: int) -> list | deque:
        res = deque([])
        while num > 0:
            res.appendleft(num % 2)
            num //= 2

        return res

    def get_flag(self, pos: int) -> bool:
        if self.position_validate(pos):

            bin = self.int2bin(self.flags)
            if len(bin) < 8:
                lst = [0] * (8 - len(bin))
                bin = lst + bin

            return bool(bin[pos])

        else:
            raise ValueError(f'Position must be between {Byte.min_pos} and {Byte.max_pos}')

    def set_flag(self, pos: int, val: bool):
        if self.position_validate(pos):
            bin = self.int2bin(self.flags)
            if len(bin) < 8:
                lst = [0] * (8 - len(bin))
                bin = lst + bin
            bin[pos] = int(val)
            self.flags = self.bin2int(bin)
        else:
            raise ValueError(f'Position must be between {Byte.min_pos} and {Byte.max_pos}')