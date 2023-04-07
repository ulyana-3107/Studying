def ladders(n, curr=[]):
    if sum(curr) == n:
        return [curr]
    elif sum(curr) > n:
        return []
    else:
        res = []
        for i in range(curr[-1] + 1 if curr else 1, n + 1):
            res += ladders(n, curr + [i])
        return res


def count_number_of_ladders(n: int) -> int:
    all_ladders = ladders(n)
    return len(all_ladders)


print(ladders(6))

# for i in range(3, 6):
#     print(f'{i} steps: {count_number_of_ladders(i)} ladders')
