# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such
# that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.


def get_max_sum(arr: list) -> int:
    n = len(arr)
    swapped = True
    s, e = 0, n
    while swapped:
        swapped = False
        for i in range(s, e - 1):
            if arr[i + 1] < arr[i]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                swapped = True
        if not swapped:
            break
        e -= 1
        for i in range(e - 1, -1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        s += 1
    print(arr)
    summ, ind = 0, 0
    while ind < n - 1:
        sub_arr = arr[ind: ind + 2]
        if sub_arr[0] <= sub_arr[1]:
            summ += sub_arr[0]
            ind += 2
            continue
        summ += sub_arr[1]
        ind += 2
    return summ


a = [5, 1, -7, 3, 1, 9, 8, 9, 0, -1]
a1 = [1, 4, 3, 2]  # 4
a2 = [6, 2, 6, 5, 1, 2]  # 9
print(get_max_sum(a2))
