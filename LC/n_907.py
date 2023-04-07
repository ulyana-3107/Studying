from collections import deque


class Solution:
    def sumSubarrayMins(self, arr: list) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        sum_of_minimums = 0
        for i in range(len(arr) + 1):  # O(N + 1) where N is len(arr) -> O(N)
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):  # O(1)
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i
                count = (mid - left_boundary) * (right_boundary - mid)
                sum_of_minimums += (count * arr[mid])

            stack.append(i)

        return sum_of_minimums % MOD
# O(N) * O(1) -> O(N).


def sub_sets_generator(arr):
    l, array = len(arr), []
    options = l
    for size in range(1, l + 1):
        i = 0
        while i != options:
            sub_arr = arr[i: i + size]
            i += 1
            yield sub_arr
        options -= 1


def first_approach(array: list) -> int:
    l, arr, c = len(array), [], 0
    for i in range(l):  # O(N)
        max_plus = l - i
        for j in range(1, max_plus + 1):  # O(N)
            start, end = i, i + j
            new = array[start:end]  # O(N)
            arr.append(new)
            c += min(new)
    return c
#  O(N**2) + O(N) -> O(N**2)


def second_approach(A: list) -> int:
    l, res = len(A), 0
    iter_object = sub_sets_generator(A)  # O(1) ?
    for case in range(l*(l + 1)//2):  # (O(N) * O(N+1))//2 -> O(N**2)
        res += min(next(iter_object))  # O(N)
    return res
    # O(1?) + O(N**2) * O(N) -> O(N**3)


def third_approach(arr: list) -> int:
    c, n, arr_ = 0, len(arr), []
    for start in range(n):  # O(N)
        for end in range(n, start - 1, -1):  # O(N - 1) -> O(N)
            sub_arr = arr[start: end]  # O(N)
            if len(sub_arr):
                c += min(sub_arr)  # O(N) - worst case (in most cases < N)
    return c
# O(N) * O(N) * O(N) + (O(1) + max(O(N), O(1)) -> O(N**3)


def way1(arr: list) -> list:
    result, l, added = list(), len(arr), set()
    for elem_index in range(l):  # O(N)
        elem = arr[elem_index]
        left_part, right_part = [], []
        if elem in added and len(set(arr[:elem_index + 1])) == 1:  # O(N**2) (преобразование в сет + срез)
            for i in range(elem_index + 1, l):  # O(N)
                if arr[i] < elem:
                    break
                else:
                    right_part += [arr[i]]
            sub_arr = [elem] + right_part
        else:
            for i in range(elem_index - 1, -1, -1):  # O(N)
                if arr[i] <= elem:
                    break
                else:
                    left_part = [arr[i]] + left_part
            for i in range(elem_index + 1, l):  # O(N)
                if arr[i] < elem:
                    break
                else:
                    right_part.append(arr[i])
            sub_arr = left_part + [elem] + right_part  # O(N)
        result.append([elem, sub_arr])
        added.add(elem)
    return result
# O(N)*O(N**2) -> O(N**3).


# def way2(arr: list) -> dict:
#     result_dict, l = dict(), len(arr)
#     for i in range(len(arr)):
#         if i == 0:
#             sub_arr = [arr[i]]
#             for j in range(1, l):
#                 if arr[j] < arr[i]:
#                     break
#                 else:
#                     sub_arr.append(arr[j])
#         elif i == l - 1:
#             sub_arr = [arr[i]]
#             for g in range(l - 2, -1, -1):
#                 if arr[g] < arr[i]:
#                     break
#                 else:
#                     sub_arr = [arr[g]] + sub_arr
#         else:
#             sub_left, sub_right = deque([]), []
#             for j in range(i - 1, -1, -1):
#                 if arr[j] < arr[i]:
#                     break
#                 else:
#                     sub_left.appendleft(arr[j])
#             for j in range(i + 1, l):
#                 if arr[j] < arr[i]:
#                     break
#                 else:
#                     sub_right.append(arr[j])
#             sub_arr = list(sub_left) + [arr[i]] + sub_right
#         result_dict[arr[i]] = sub_arr
#     return result_dict


def split_into_three(sub_arr: list, elem: int) -> tuple:
    first, second, third, l = [], [], [], len(sub_arr)
    i = 0
    while sub_arr[i] != elem:  # O(N) - worst case
        first.append(sub_arr[i])
        i += 1
    i += 1
    while i != l:  # O(N - 1) -> O(N)
        third.append(sub_arr[i])
        i += 1
    second = [elem]
    return first, second, third
    # O(N) + O(N) -> O(2N) -> O(N).


def min_max(arr: list) -> list:
    if not len(arr):
        return [arr]
    res = []
    for i in range(len(arr) + 1):  # O(N)
        res.append(arr[0: i])  # O(N)
    return res
    # O(1) + max(O(1), O(N**2)) -> O(N**2)


def max_min(arr: list) -> list:
    if not len(arr):
        return [arr]
    res = []
    for i in range(len(arr), -1, -1):
        res.append(arr[0: i])
    return res
    # O(1) + max(O(1), O(N**2)) -> O(N**2)


def count_way1(sub_arrs) -> list:
    result = list()
    for elem, sub_arr in sub_arrs:  # O(N)
        first, second, third = split_into_three(sub_arr, elem)
        counter = 0
        left_parts, right_parts = max_min(first), min_max(third)  # O(N**2) + O(N**2) -> O(N**2)
        for i in range(len(left_parts) - 1, -1, -1):  # O(N)
            for j in right_parts:  # O(N)
                massiv = left_parts[i] + second + j  # O(1)
                if min(massiv) == elem:
                    counter += 1
                else:
                    break
        result.append([elem, counter])
    return result
# O(N) * (O(N**2) + O(N**2)) -> O(N) * O(N**2) -> O(N**3)


def count_way2(sub_arrs: list) -> list:
    res = list()
    for elem, arr in sub_arrs:  # O(N)
        l = len(arr)  # O(1)
        for i in range(l):  # O(N) - worst case
            if arr[i] == elem:  # O(1)
                num1, num2 = i + 1, l - i  # O(1)
                res.append([elem, num1*num2])
                break
    return res
    # O(N) * (O(1) + O(N)) -> O(N**2).


def fourth_approach(arr: list) -> int:
    c, l = 0, len(arr)
    if arr == sorted(arr) and len(set(arr)) == len(arr):  # O(NlogN) + O(N) -> O(NlogN)
        for i in range(l):  # O(N)
            c += arr[i]*(l-i)
        return c
    elif sorted(arr) == reversed(arr):  # O(NlogN) + O(N) -> O(NlogN)
        for i in range(l):  # O(N)
            c += arr[l - i - 1] * (l - i)
        return c
    else:
        sub_arrs = way1(arr)  # O(N**2)
        dict_, c = count_way2(sub_arrs), 0  # O(N**2)/O(N**3)
        # count_way2 is possible too
        for k, v in dict_:  # O(N)
            c += k*v
        return c
# O(NlogN) + max(O(N), O(N*NlogN), (O(N**2) + O(N**2) + O(N))) -> O(N**2logN).


a1, a2, a3, a4, a5 = [1 for i in range(4)], [1, 2, 1, 2], [1, 2, 2, 2, 1], [i for i in range(5, -1, -1)], \
    [0, 3, 8, 5, -3]
print(' 1      2      3      4\n')
for i in range(1, 6):
    name = 'a' + str(i)
    print(first_approach(eval(name)), end=' ')
    print('---', second_approach(eval(name)), end=' ')
    print('---', third_approach(eval(name)), end=' ')
    print('---', fourth_approach(eval(name)), end=' ')
    print('\n')


# if not len(left_parts) and not len(right_parts):
        #     result_dict[elem] = counter + 1
        #     continue
        # elif not len(left_parts):
        #     for part in right_parts:
        #         massiv = second + part
        #         if min(massiv) == elem:
        #             counter += 1
        #         else:
        #             break
        # elif not len(right_parts):
        #     for i in range(len(left_parts) - 1, -1, -1):
        #         massiv = left_parts[i] + second
        #         if min(massiv) == elem:
        #             counter += 1
        #         else:
        #             break


# else:
        #     for i in range(elem_index, -1, -1):
        #         if min([arr[i]] + left_part) == elem:
        #             left_part = [arr[i]] + left_part
        #         else:
        #             break
        #     for i in range(elem_index, l):
        #         if min(right_part + [arr[i]]) == elem:
        #             right_part += [arr[i]]
        #         else:
        #             break
        #     sub_arr = left_part + right_part[1:]