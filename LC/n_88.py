# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


def solution(nums1: list, m: int, nums2: list, n: int) -> list:
    for i in range(n):
        nums1[m + i] = nums2[i]
        if nums1[m + i] < nums1[m + i - 1]:
            for j in range(m + i -1, -1, -1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
    print(nums1)


solution([1, 4, 9, 0, 0, 0], 3, [3, 2, 7], 3)
