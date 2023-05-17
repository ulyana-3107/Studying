# Дана 1 функция в виде таблицы истинности. Используя решение 3, проверить её на тавтологию, выполнимость,
# тождественную ложь


def check_function(func: list) -> None:

    tautology = all(func)
    # противоречивость
    inconsistency = not any(func)
    duable = any(func)

    print(f'Tautology: {tautology}')
    print(f'Inconsistency: {inconsistency}')
    print(f'Duable: {duable}')



if __name__ == '__main__':
    check_function([1, 0, 0])
