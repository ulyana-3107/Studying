from itertools import combinations


# Дано n функций в виде таблиц истинности.
# 1)Проверить логическое следствие (Из n-1 функций следует последняя)
# 2)Найти всевозможные пары (и больших размерностей) логических следствий.
# (Например, из f1 -> f2 и f1,f2 -> f3 и так далее).


def logical_consequence(*functions: list) -> bool:
    """
    Returns True, if functions[-1] is the logical sequence of functions[:-1]
    """
    prev = []
    last = None

    for ind in range(len(functions)):
        if ind == len(functions) - 1:
            last = functions[ind]
        else:
            prev.append(functions[ind])

    for i in range(len(last)):
        values = [arr[i] for arr in prev]
        if all(values) and not last[i]:
            return False

    return True


def fact(num: int) -> int:
    if num == 1:
        return 1
    return num * fact(num - 1)


def all_pairs(*functions) -> None:
    n = len(functions)

    for i in range(n - 1, 0, -1):
        combs = combinations(range(1, n + 1), i)
        times = int(fact(n)/fact(i)/fact(n - i)) if i > 1 else n

        for j in range(times):
            indexes = next(combs)
            rest = [_ for _ in range(1, n + 1) if _ not in indexes]
            funcs_ = [functions[i - 1] for i in indexes]

            if len(rest) == 1:
                funcs = funcs_ + [functions[rest[-1] - 1]]

                if logical_consequence(*funcs):
                    print(f'{funcs[: -1]} -> {funcs[-1]}')

            else:
                for k in range(len(rest)):
                    funcs = funcs_ + [functions[rest[k] - 1]]

                    if logical_consequence(*funcs):
                        print(f'{funcs[:-1]} -> {funcs[-1]}')


if __name__ == '__main__':
    arr1, arr2 = [0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1]
    arr3 = [1, 1, 1, 1, 0, 1, 1, 1]
    print(logical_consequence(arr1, arr2, arr3))
    # arr1 = [1, 0, 1, 0]
    # arr2 = [0, 1, 0, 1]
    # arr3 = [1, 1, 0, 0]
    # print(all_pairs(arr1, arr2, arr3))
