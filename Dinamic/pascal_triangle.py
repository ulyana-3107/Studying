def triangle(num_rows: int) -> list:
    res = [[1]]
    for i in range(num_rows - 1):
        prev = res[-1]
        new = []
        for j in range(len(prev) + 1):
            if j == 0 or j == len(prev):
                new.append(1)
            else:
                new.append(prev[j - 1] + prev[j])
        res.append(new)
    return res


print(triangle(4))