# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not
# exist, return the maximum number.


def thirdMax(arr: list) -> int:
    if len(arr) < 4:
        if len(set(arr)) == len(arr) and len(arr) == 3:
            return min(arr)
        else:
            return max(arr)
    else:
        n = len(arr)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        arr_unique = []
        visited = set()
        for elem in arr:
            if elem not in visited:
                arr_unique.append(elem)
                visited.add(elem)
        if len(arr_unique) > 2:
            return arr_unique[-3]
        else:
            return max(arr_unique)


seq = [3, 2, 1]  # 1
s2 = [1, 2]  # 2
s3 = [2, 2, 3, 1]  # 1
print(thirdMax(s3))