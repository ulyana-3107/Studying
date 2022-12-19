from sortedcontainers import SortedList
import itertools
import time
import random


def my_solution(array) -> int:
    few_arrays, l = [], len(array)
    for sub_len in range(1, l + 1):
        if sub_len == l:
            few_arrays.append(SortedList(array)[0])
        else:
            times = l - sub_len + 1
            for t in range(times):
                few_arrays.append(SortedList(array[t: t + sub_len])[0])
    return sum(few_arrays)

def normal_solution(array):
    res = 0
    stack = []
    array = [float('-inf')] + array + [float('-inf')]
    for i, n in enumerate(array):
        while stack and array[stack[-1]] > n:
            cur = stack.pop()
            res += array[cur] * (i - cur) * (cur - stack[-1])
        stack.append(i)
    return res % (10 ** 9 + 7)


a1, a2, a3 = [1, 3, 8, 9], [1, 2, 3, 4], [1, 3, 8, 12, 14]
# r1, r2, r3 = 38, 20, 79
a4 = [random.randint(1, 10001) for i in range(500)]
test_collection = [a1,a2, a3,a4]
for test in test_collection:
    t1 = time.time()
    res = my_solution(test)
    t2 = time.time()
    print(f'my_res: {res}, time: {t2 - t1}')
    res = normal_solution(test)
    print(f'other_res: {res}, time: {time.time() - t2}\n')