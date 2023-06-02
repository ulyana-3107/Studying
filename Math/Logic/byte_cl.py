# Создать класс с одним полем flags типа int (считаем, что он не более 1 байта [-128, 127]). Реализовать методы для
# работы со значениями флагов (всего 8 штук - 1 бит = 1 флаг). Что-то вроде функции get_flag(position: int) -> boolean,
# set_flag(position: int, val: boolean).


class Byte:
    def __init__(self, flags: list = None):
        if not flags:
            self.flags = [0] * 8
        else:
            self.flags = flags

    def get_flag(self, pos: int) -> bool:
        return bool(self.flags[pos - 1])

    def set_flag(self, pos: int, val: bool):
        self.flags[pos - 1] = int(val)


if __name__ == '__main__':
    b = Byte([0, 0, 1, 1, 0, 0, 1, 1])
    print(b.get_flag(4))
    b.set_flag(4, False)
    print(b.get_flag(4))