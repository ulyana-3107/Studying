from itertools import combinations


#  source code:
# from itertools import permutations
# def combinations(iterable, r):
#     pool = tuple(iterable)
#     n = len(pool)
#     for indices in permutations(range(n), r):
#         if sorted(indices) == list(indices):
#             yield tuple(pool[i] for i in indices)


# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)


def factorial(n: int) -> int:
    temp = 1
    current = 2
    for i in range(n - 1):
        temp = temp * current
        current += 1
    return temp


test = [1, 2, 3, 4, 5]
# r, n = 4, len(test)
#
# if r != 0 and r < n:
#     r_fact, n_fact, n_minus_r_fact = factorial(r), factorial(n), factorial(n - r)
#     print(f'n! - {n_fact}, r! - {r_fact}, (n - r)! - {n_minus_r_fact}')
#     times = n_fact//r_fact//n_minus_r_fact
# else:
#     times = 0
# result = combinations(test, r)
# print(times)
# for i in range(times):
#     print(next(result))


res = list(combinations(test, 4))
print(res)