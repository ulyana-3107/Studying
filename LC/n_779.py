# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at
# the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.


def k_th_number(n: int, k: int, start: list = [0], db: dict = {'1': [1, 0], '0': [0, 1]}) -> int:
    if n == 1:
        return start[k - 1]
    else:
        if len(start) == 1:
            new_part = db[str(start[-1])]
            return k_th_number(n - 1, k, new_part, db)

        new_part = start.copy()
        last_part = ''.join(str(i) for i in start[len(start)//2:])
        if last_part in db:
            new_part.extend(db[last_part])
            return k_th_number(n - 1, k, new_part, db)
        curr = []
        s = ''
        i = 0

        while i != len(last_part):
            s += last_part[i]
            i += 1
            if s not in db:
                seq = [int(i) for i in db[s[: -1]]]
                new_part.extend(seq)
                i -= 1
                s = ''
                curr.extend(seq)
        new_part.extend(db[s])
        curr.extend(db[s])
        db[last_part] = curr

        return k_th_number(n - 1, k, new_part, db)


def kthGrammar(n: int, k: int) -> int:
    # n=1: 0
    # n=2: 0 1
    # n=3: 0 1 1 0
    # n=4: 0 1 1 0 1 0 0 1
    # n=5: 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0
    # n=6: 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1
    # row(n) = row(n-1) + flipped(row(n-1))
    if n == 1:
        return 0
    if n == 2:
        return k - 1
    # n == 3, then length == 4 == 1<<(n-1)
    half = 1<<(n-2)
    if k <= half:
        return kthGrammar(n-1, k)
    else:
        return int(not kthGrammar(n-1, k - half))


if __name__ == '__main__':
    n1, k1 = 1, 1  # 0
    n2, k2 = 2, 1  # 0
    n3, k3 = 2, 2  # 1
    n4, k4 = 5, 10  # 0
    n5, k5 = 4, 8  # 1

    for i in range(1, 6):
        print(k_th_number(eval('n' + str(i)), eval('k' + str(i))), kthGrammar(eval('n' + str(i)), eval('k' + str(i))))