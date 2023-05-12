def minimum_cost(axis: list) -> int:
    n = len(axis)

    if n <= 3:
        if n == 3:
            return axis[2] - axis[1] + (axis[1] - axis[0])
        else:
            return axis[1] - axis[0]
    else:
        rates = {1: axis[1] - axis[0], 2: axis[2] - axis[1] + axis[1] - axis[0]}

        for i in range(3, n):
            rates[i] = min(rates[i - 2], rates[i - 1]) + axis[i] - axis[i - 1]

        return round(rates[n - 1], 2)


def minimum_cost_2(seq: list) -> int:
    diff = [seq[0], seq[1] - seq[0], seq[2] - seq[1] + seq[1] - seq[0]]

    for i in range(3, len(seq)):
        diff.append(seq[i] - seq[i - 1] + min(diff[-1], diff[-2]))

    return round(diff[-1], 2)


def rec_solution(seq, i, db: dict):
    if i in db:
        return db[i]
    if i == 1:
        db[i] = seq[1] - seq[0]
    elif i == 2:
        db[i] = seq[2] - seq[1] + seq[1] - seq[0]
    else:
        db[i] = seq[i] - seq[i-1] + min(rec_solution(seq, i - 1, db), rec_solution(seq, i - 2, db))
    return round(db[i], 2)


if __name__ == '__main__':
    axis_2 = [1, 2]  # 1
    axis_1 = [1, 3, 8]  # 7
    axis0 = [0, 2, 4, 10, 12]  # 6
    axis1 = [11, 12, 13, 16, 17]  # 3
    axis2 = [6.34, 6.82, 15.89, 24.58]  # 9.16
    axis3 = [11, 12, 14, 16, 18]  # 5
    axis4 = [11, 13, 14, 17, 21]  # 7

    for n in range(5):
        arr = eval('axis'+str(n))
        i = len(arr) - 1
        print(rec_solution(arr, i, {}))
