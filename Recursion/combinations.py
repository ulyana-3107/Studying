def combinations(lst, n):
    if n == 0:
        return [[]]
    l = []
    for j in range(len(lst)):
        empty = lst[j]
        rec_lst = lst[j + 1:]

        for x in combinations(rec_lst, n - 1):
            l.append([empty] + x)

    return l


if __name__ == '__main__':
    array = list(range(1, 6))
    print(combinations(array, 3))