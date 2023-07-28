def find_index(lst:list) -> int:
    l, r = 0, len(lst) - 1

    while l <= r:
        middle = (l + r) // 2
        if lst[middle] == middle:
            return middle
        elif lst[middle] < middle:
            l = middle + 1
        else:
            r = middle - 1

    return - 1


if __name__ == '__main__':
    l1 = [0, 3, 5]
    l2 = [1, 2, 4]
    l3 = [-2, -1, 0, 3, 4, 6, 8]

    print(find_index(l1))
    print(find_index(l2))
    print(find_index(l3))

    # O(logN), N = len(list)
