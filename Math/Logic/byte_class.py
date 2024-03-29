# Создать класс с одним полем flags типа int (считаем, что он не более 1 байта [-128, 127]). Реализовать методы для
# работы со значениями флагов (всего 8 штук - 1 бит = 1 флаг). Что-то вроде функции get_flag(position: int) -> boolean,
# set_flag(position: int, val: boolean).
from collections import deque


class Byte:
    min_pos, max_pos = 0, 7

    @classmethod
    def position_validate(cls, pos) -> bool:
        return cls.min_pos <= pos <= cls.max_pos

    def __init__(self, flags: int = 0):
        self.flags = flags

    def get_flag(self, pos: int) -> bool:
        if self.position_validate(pos):
            var = int(str((self.flags >> pos) & 1)[-1])
            return bool(var)

        else:
            raise ValueError(f'Position must be between {Byte.min_pos} and {Byte.max_pos}')

    def set_flag(self, pos: int, val: bool):
        if self.position_validate(pos):
            if not self.get_flag(pos) == val:
                self.flags = self.flags ^ (1 << pos)
        else:
            raise ValueError(f'Position must be between {Byte.min_pos} and {Byte.max_pos}')


if __name__ == '__main__':
    b = Byte()
    print(b.get_flag(4))
    b.set_flag(4, True)
    print(b.get_flag(4))
    b.set_flag(4, False)
    print(b.get_flag(4))