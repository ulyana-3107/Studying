from __future__ import annotations
from itertools import combinations


def all_subsequences(sequence: list) -> list:
    result_seq, l = [], len(sequence)
    for i in range(l):
        rest_num = l - i
        for j in range(rest_num):
            sub_arr = sequence[i + 1:i + j + 1]
            new_seq = [sequence[i]] + sub_arr
            result_seq.append(new_seq)
    return result_seq


def fact(n: int) -> int:
    diff_param = n
    n -= 1
    for i in range(n - 1):
        diff_param = diff_param * n
        n -= 1
    return diff_param


def num_of_ladders(n: int) -> tuple:
    arr, counter = [], 0
    if n in (1, 2):
        return [n], 1
    elif n % 2:
        first_max = int(n/2)
    else:
        first_max = int(n/2) - 1
    for i in range(1, first_max + 1):
        if i == n:
            counter += 1
            arr.append({i})
        else:
            rest = [_ for _ in range(i + 1, n)]
            len_rest = len(rest)
            min_, max_ = 1, len_rest//2 + 1
            for _ in range(min_, max_):
                iterator = combinations(rest, _)
                times = fact(len_rest)//fact(_)//fact(len_rest - _)
                for t in range(times):
                    next_ = next(iterator)
                    if i + sum(next_) == n:
                        to_add = set([i] + list(next_))
                        if to_add not in arr:
                            arr.append(to_add)
                            counter += 1
    arr.append({n})
    counter += 1
    return arr, counter


def get_result(n: int, proof: bool = False) -> tuple | int:
    result = num_of_ladders(n)
    if proof:
        return result
    else:
        return result[1]


test_cases = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 8, 10: 10}
for num, result in test_cases.items():
    res = get_result(num, proof=True)
    print(f'number: {num}\n result: {res}\n R/W: {res[1] == result}\n', '*'*20+'\n\n')

for i in (11, 12, 13, 14, 15, 16, 17):
    print(get_result(i))


# max start number:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in numbers:
#     r = abs(n % 2 - 1)
#     m = n//2 - r
#     print(f'{n} - {m}\n')

