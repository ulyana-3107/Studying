# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
# be unique, and you may return the result in any order.

def solution(arr1: list, arr2: list) -> list:
    result = []
    n = len(arr1)
    m = len(arr2)
    i = j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1
    return result


print(solution([1, 3, 5, 2, 4], [1, 5, 7, 9]))
