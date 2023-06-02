# Дано число n. Реализовать быстрое:
# Возведение 2 в степень n
# Возведение 4 в степень n
# Возведение 2 в степени m в степень n


from collections import deque


def int_to_binary(int_num: int) -> deque:
    binary = deque([])

    while int_num > 0:
        binary.appendleft(int_num % 2)
        int_num = int_num // 2

    return binary


def binary_to_int(bin_num: deque) -> int:
    bin_num = list(bin_num)
    res, i = 0, 0

    while bin_num:
        res += bin_num.pop() * 2 ** i
        i += 1

    return res


def exponentiation_of_two1(pow: int) -> int:
    bin_num = int_to_binary(2)
    zeros = [0] * (pow - 1)
    bin_num.extend(zeros)
    int_num = binary_to_int(bin_num)

    return int_num


def exponentiation_of_four1(pow: int) -> int:
    binary = int_to_binary(4)
    zeros = [0, 0] * (pow - 1)
    binary.extend(zeros)

    return binary_to_int(binary)


def double_exponentiation1(pow1: int, pow2: int) -> int:
    binary = int_to_binary(2)
    zeros = [0] * (pow1 * pow2 - 1)
    binary.extend(zeros)
    return binary_to_int(binary)


def exponentiation_of_two2(pow: int) -> int:
    return 2 << pow - 1


def exponentiation_of_four2(pow: int) -> int:
    return 2 << pow * 2 - 1


def double_exponentiation2(pow1: int, pow2: int) -> int:
    return 2 << pow1 * pow2 - 1
