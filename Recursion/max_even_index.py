

def find_index(lst: list, i1, i2, checked=False) -> int:
    if lst[0] % 2 and not checked:
        return -1
    elif not lst[-1] % 2 and not checked:
        return len(lst) - 1

    else:
        dist = i2 - i1
        mid = i1 + (dist//2)
        mid_even = not lst[mid] % 2
        if mid_even:
            if lst[mid + 1] % 2:
                return mid
            else:
                i1, i2 = mid + 1, i2
                return find_index(lst, i1, i2, True)
        else:
            i1, i2 = i1, mid
            return find_index(lst, i1, i2, True)


# O(logN), N - len(list).


lst1 = [1, 3, 5]
lst2 = [2, 1, 1, 1, 3, 5, 7]
lst3 = [2, 2, 2, 2, 9]
lst4 = [2, 4, 6, 7, 9, 9]

if __name__ == '__main__':
    name = 'lst'
    for i in range(1, 5):
        arr = eval(f'{name}{str(i)}')
        res = find_index(arr, 0, len(arr))
        print(arr, res, sep=' - ')