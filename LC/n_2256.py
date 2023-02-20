from math import ceil, floor
from collections import deque


class Solution:
    def minimumAverageDifference(self, nums) -> int:
        miniAverage = float("inf")
        left = 0
        s = sum(nums)
        res = 0
        for i, num in enumerate(nums):  # O(N)
            left += num
            right = s - left
            if i != len(nums) - 1:
                if abs(left // (i + 1) - right // (len(nums) - i - 1)) < miniAverage:
                    miniAverage = abs(left // (i + 1) - right // (len(nums) - i - 1))
                    res = i
            else:
                if left // (i + 1) < miniAverage:
                    res = i
        return res
# O(N).


def first_approach(arr: list) -> int:
    len_, m, res = len(arr), float('inf'), 0
    for i in range(len(arr)):  # O(N)
        f_num, s_num, f_part, s_part = i + 1, len_ - i - 1, [], deque([])
        ind = 0
        while ind != f_num:  # O(N) - worst case
            f_part.append(arr[ind])
            ind += 1
        ind2, c = len_ - i - 1, 0
        while ind2 != 0:  # O(N) - worst case
            s_part.appendleft(arr[len_ - 1 - c])
            ind2 -= 1
            c += 1
        if len(f_part):
            num1 = floor(sum(f_part)/len(f_part))
        else:
            num1 = 0
        if len(s_part):
            num2 = floor(sum(s_part)/len(s_part))
        else:
            num2 = 0
        diff = abs(num1 - num2)
        if diff < m:
            res, m = i, diff
    return res
# O(N) * (O(N) + O(N)) -> O(N**2).


def second_approach(nums: list) -> int:
    res, min_aver, l_ = 0, float('inf'), len(nums)
    l_part, r_part = 0, sum(nums)
    for i, num in enumerate(nums):  # O(N)
        if i == l_ - 1:
            l_part += num
            num = abs(ceil(l_part/l_))
            if num < min_aver:
                res = i
        else:
            l_part += num
            r_part -= num
            num1, num2 = i + 1, l_ - i - 1
            num1_, num2_ = floor(l_part/num1), floor(r_part/num2)
            av_diff = abs(num1_ - num2_)
            if av_diff < min_aver:
                res = i
                min_aver = av_diff
    return res
# O(N).


def split_arr(arr, n):
    for i in range(n):  # O(N)
        a, b = i + 1, i + 1
        a_, b_ = arr[: a], arr[b:]
        yield(a_, b_)  # O(?)


def average_diff(arr) -> int:
    n = len(arr)
    if n < 2:
        return int(False)
    res, res_ = split_arr(arr, n), []
    for i in range(n):  # O(N)
        next_ = next(res)
        a, b, a_, b_ = next_[0], next_[1], len(next_[0]), len(next_[1])
        _a = floor(sum(a)/a_) if a_ > 0 else 0
        _b = floor(sum(b)/b_) if b_ > 0 else 0
        res_.append(abs(_a - _b))
    m = 0
    for i_ in range(1, n):
        if res_[i_] < res_[m]:
            m = i_
    return m
# O(1) + max(O(1), (O(N) + O(N)) -> O(N).


t1, t2, t3, t4, t5 = ([1, 2, 8, 3, 4], 2), ([5, 3, 2], 1), ([1, 2, 3, 4], 0), ([1, 2, 3], 0), ([2, 4, 5, 9, 3], 1)
for i in range(1, 6):
    name = eval('t'+str(i))
    print(average_diff(name[0]), '--', first_approach(name[0]), '---', second_approach(name[0]))
    print('\n\n')
    # print(res, res == name[1], end=' ***** ')
#
# class Solution:
#     def minimumAverageDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = -1
#         min_avg_diff = math.inf
#
#         for index in range(n):
#             # Calculate average of left part of array, index 0 to i.
#             left_part_average = 0
#             for i in range(index + 1):
#                 left_part_average += nums[i]
#             left_part_average //= (index + 1)
#
#             # Calculate average of right part of array, index i+1 to n-1.
#             right_part_average = 0
#             for j in range(index + 1, n):
#                 right_part_average += nums[j]
#
#             # If right part have 0 elements, then we don't divide by 0.
#             if index != n - 1:
#                 right_part_average //= (n - index - 1)
#
#             curr_difference = abs(left_part_average - right_part_average)
#
#             # If current difference of averages is smaller,
#             # then current index can be our answer.
#             if curr_difference < min_avg_diff:
#                 min_avg_diff = curr_difference
#                 ans = index
#
#         return ans

# Accepted (fits into the time frame)
# class Solution:
# 	def minimumAverageDifference(self, nums: List[int]) -> int:
# 		miniAverage = float("inf")
# 		left = 0
# 		s = sum(nums)
# 		res = 0
# 		for i, num in enumerate(nums):
# 			left += num
# 			right = s - left
# 			if i != len(nums) - 1:
# 				if abs(left // (i + 1) - right // (len(nums) - i - 1)) < miniAverage:
# 					miniAverage = abs(left // (i + 1) - right // (len(nums) - i - 1))
# 					res = i
# 			else:
# 				if left // (i + 1) < miniAverage:
# 					res = i
# 		return res


