# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
# appear as many times as it shows in both arrays and you may return the result in any order.


def solution(arr1: list, arr2: list) -> list:
    arr1.sort()
    arr2.sort()
    n, m, res = len(arr1), len(arr2), []
    i = j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            res.append(arr1[i])
            i += 1
            j += 1
    return res


s1, s2 = [0, 3, 6, 2], [2, 3, 7, 8]
print(solution(s1, s2))
