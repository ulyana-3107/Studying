from collections import deque


def binary_to_decimal(n: list | deque) -> int:
    num = len(n)
    res = 0

    for i in range(num):
        res += n[i] * 2 ** (num - i - 1)

    return res


def decimal_to_binary(n: int | float) -> deque:
    binary = deque()

    while n > 0:
        binary.appendleft(n % 2)
        n = n // 2

    return binary


def decimal_to_hexadecimal(n: int) -> deque:
    letters = 'abcdef'
    nums = [i for i in range(10, 16)]
    d = {num: letter for num, letter in zip(nums, letters)}
    hexa_d = deque()

    while n > 0:
        rest = n % 16
        if rest > 10:
            rest = d[rest]

        hexa_d.appendleft(rest)
        n = n //16

    return hexa_d


def hexadecimal_to_decimal(n: str) -> int:
    d = {}
    n_ = 10
    for letter in 'abcdef':
        d[letter] = n_
        n_ += 1

    l = len(n)
    l_ = l
    decimal = 0

    while l_ != 0:
        num = n[l - l_]
        if num.lower() in d:
            num = d[num]
        else:
            num = int(num)
        decimal += num * 16 ** (l_ - 1)

        l_ -= 1

    return decimal


def octal_to_decimal(n: int) -> int:
    n = str(n)
    l = len(n)
    l_ = l
    decimal = 0

    while l_ != 0:
        num = int(n[l - l_])
        decimal += num * 8 ** (l_ - 1)
        l_ -= 1

    return decimal


def decimal_to_octal(n: int) -> deque:
    octal = deque()
    while n > 0:
        octal.appendleft(n % 8)
        n = n//8

    return octal


if __name__ == '__main__':
    print(octal_to_decimal(321))
