from math import ceil


def split_arr(arr, n):
    for i in range(n):
        a, b = i + 1, i + 1
        a_, b_ = arr[: a], arr[b:]
        yield(a_, b_)

def average_diff(arr) -> int:
    n = len(arr)
    if n < 2:
        return int(False)
    res, res_ = split_arr(arr, n), []
    for i in range(n):
        next_ = next(res)
        a, b, a_, b_ = next_[0], next_[1], len(next_[0]), len(next_[1])
        _a = ceil(sum(a)//a_) if a_ > 0 else 0
        _b = ceil(sum(b)//b_) if b_ > 0 else 0
        res_.append(abs(_a - _b))
    m = 0
    for i_ in range(1, n):
        if res_[i_] < res_[m]:
            m = i_
    return m

t1, t2, t3, t4, t5 = ([1, 2, 8, 3, 4], 2), ([5, 3, 2], 1), ([1,2, 3, 4], 0), ([1, 2, 3], 0), ([2, 4, 5, 9, 3], 1)
for i in range(1, 6):
    name = eval('t'+str(i))
    res = average_diff(name[0])
    print(res, res == name[1], end=' ***** ')

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


