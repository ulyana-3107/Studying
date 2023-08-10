def find_index(arr, elem):
    n = len(arr)
    l, r = 0, n - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == elem:
            return mid

        elif arr[mid] < arr[r]:
            if arr[mid] < elem <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1

        else:
            if arr[l] <= elem < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1

    return -1


if __name__ == '__main__':
    l1 = [3, 4, 5, 6, 0, 1, 2]
    l2 = [5, 6, 2, 4]
    r1, r2 = find_index(l1, 0), find_index(l2, 5)
    print(r1, r2)

