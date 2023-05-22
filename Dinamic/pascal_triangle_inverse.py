def get_row(n: int) -> list:
    res = [1]
    for i in range(n):
        new = []
        for j in range(len(res) + 1):
            if j in (0, len(res)):
                new.append(1)
            else:
                new.append(res[j - 1] + res[j])
        res = new
    return res


print(get_row(4))
