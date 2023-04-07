<<<<<<< HEAD
from __future__ import annotations


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def is_empty(matrix) -> bool:
    for arr in matrix:
        if any(arr):
            return False
    return True


def is_diagonal(matrix) -> bool:
    for ind in range(len(matrix)):
        arr = matrix[ind]
        arr_ = [arr[i] for i in range(len(arr)) if i != ind]
        if not any(arr_) and bool(arr_[ind]):
            continue
        else:
            return False
    return True


def fact(n: int) -> int:
    temp, res = 1, 1
    for i in range(n):
        temp = temp * res
        res += 1
    return temp


def ppl_acquantancies(matrix) -> dict:
    res = dict()
    for i in range(len(matrix)):
        arr = matrix[i]
        known = [i for i in range(len(arr)) if arr[i] != 0]
        res[i] = set(known)
    return res


def ppl_split(matrix) -> bool:
    n = len(matrix)
    if n < 3 or is_empty(matrix) or is_diagonal(matrix):
        return True
    else:
        known = ppl_acquantancies(matrix)
        people = set([i for i in range(1, n + 1)])
        n = len(people)
        n_fact = fact(n)
        for i in range(1, n):
            result = combinations(people, i)
            times = n_fact // fact(i) // fact(n - i)
            for t in range(times):
                first_group = set(next(result))
                second_group = people.difference(first_group)
                set_first, set_second = set(first_group), set(second_group)
                first_, second_ = True, True
                for person in first_group:
                    other = set_first.difference({person})
                    known_ = known[person]
                    if other & known_:
                        first_ = False
                        break
                for person in second_group:
                    other = set_second.difference({person})
                    known_ = known[person]
                    if other & known_:
                        second_ = False
                    break
                if first_ and second_:
                    return True
    return False


m = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
print(ppl_split(m))
=======
from __future__ import annotations


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def is_empty(matrix) -> bool:
    for arr in matrix:
        if any(arr):
            return False
    return True


def is_diagonal(matrix) -> bool:
    for ind in range(len(matrix)):
        arr = matrix[ind]
        arr_ = [arr[i] for i in range(len(arr)) if i != ind]
        if not any(arr_) and bool(arr_[ind]):
            continue
        else:
            return False
    return True


def fact(n: int) -> int:
    temp, res = 1, 1
    for i in range(n):
        temp = temp * res
        res += 1
    return temp


def ppl_acquantancies(matrix) -> dict:
    res = dict()
    for i in range(len(matrix)):
        arr = matrix[i]
        known = [i for i in range(len(arr)) if arr[i] != 0]
        res[i] = set(known)
    return res


def ppl_split(matrix) -> bool:
    n = len(matrix)
    if n < 3 or is_empty(matrix) or is_diagonal(matrix):
        return True
    else:
        known = ppl_acquantancies(matrix)
        people = set([i for i in range(1, n + 1)])
        n = len(people)
        n_fact = fact(n)
        for i in range(1, n):
            result = combinations(people, i)
            times = n_fact // fact(i) // fact(n - i)
            for t in range(times):
                first_group = set(next(result))
                second_group = people.difference(first_group)
                set_first, set_second = set(first_group), set(second_group)
                first_, second_ = True, True
                for person in first_group:
                    other = set_first.difference({person})
                    known_ = known[person]
                    if other & known_:
                        first_ = False
                        break
                for person in second_group:
                    other = set_second.difference({person})
                    known_ = known[person]
                    if other & known_:
                        second_ = False
                    break
                if first_ and second_:
                    return True
    return False


m = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
print(ppl_split(m))
>>>>>>> 7eb05628d2fb76cbafeb39d7f248f8ac1aa5442b
