def guess(num: int) -> int:
    guessed = 3
    if num < guessed:
        return -1
    elif num > guessed:
        return 1
    else:
        return 0
# O(1) + O(1) + max(O(1), O(1), O(1)) -> O(1)


def main_game(n: int) -> int:
    l, r = 1, n
    while True:
        m = (l + r)//2
        if guess(m) == -1:
            l = m + 1
        elif guess(m) == 1:
            r = m - 1
        else:
            return m

# O(log2(N - Guessed_number))


print(main_game(10))
