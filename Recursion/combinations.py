def combinations(lst, ind, n):
    if n == 0:
        return [[]]
    l = []
    for j in range(ind, len(lst)):
        empty = lst[j]

        for x in combinations(lst, ind,  n - 1):
            l.append([empty] + x)
        ind += 1

    return l


if __name__ == '__main__':
    array = list(range(1, 6))
    print(combinations(array, 0, 3))