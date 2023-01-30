def first_approach(n: int, m: int):
    if n == 1 or m == 1:
        return 1
    else:
        return first_approach(n, m - 1) + first_approach(n - 1, m)
# O(2**N)


def stack_approach(n_: int, m_: int):
    stack = [(n_, m_)]
    c = 0
    count_times = 0
    while stack:
        count_times += 1
        x, y = stack.pop()
        if x == 1 or y == 1:
            c += 1
        else:
            stack.append((x - 1, y))
            stack.append((x, y - 1))
    return c, count_times


def second_approach(n: int, m: int, dp: list) -> int:
    if 1 in (n, m):
        dp[n][m] = 1
        return 1
    if dp[n][m] == 0:
        dp[n][m] = second_approach(n - 1, m, dp) + second_approach(n, m - 1, dp)
    return dp[n][m]
# O(N*M)


# n, m = 4, 4
# dp = [[0 for i in range(n)] for j in range(m)]


def third_approach(m: int, n: int):
    count = [[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        count[i][0] = 1

    for j in range(n):
        count[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            count[i][j] = count[i - 1][j] + count[i][j - 1]
    return count[m - 1][n - 1]
# O(N*M)


def fourth_approach(p: int, q: int):
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]
# O(P*Q)


def fifth_approach(m: int, n: int):
    path = 1
    for i in range(n, (m + n - 1)):
        path *= i
        path //= (i - n + 1)
    return path
# O(M)

