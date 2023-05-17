# Даны 2 функции в виде таблиц истинности (список значений 0 и 1). Проверить их на эквивалентность.


def if_equivalent(*tr_tables) -> bool:
    i = len(tr_tables) - 1

    while i != 0:
        if tr_tables[i] != tr_tables[i - 1]:
            return False
        i -= 1

    return True


if __name__ == '__main__':

    print(if_equivalent([0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]))