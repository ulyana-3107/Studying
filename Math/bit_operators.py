from collections import deque
from count_systems import decimal_to_binary, binary_to_decimal


def and_op_decimals(a: int, b: int) -> int:
    a_binary, b_binary = decimal_to_binary(a), decimal_to_binary(b)
    result_num = []

    diff = len(a_binary) - len(b_binary)

    if diff != 0:
        s = a_binary if diff < 0 else b_binary

        for i in range(abs(diff)):
            s.appendleft(0)

    for i in range(len(a_binary)):
        result_num.append(int(a_binary[i] == 1 and b_binary[i] == 1))

    decimal_num = binary_to_decimal(result_num)

    return decimal_num


def or_op_decimals(a: int, b: int) -> int:
    a_binary, b_binary = decimal_to_binary(a), decimal_to_binary(b)
    result_num = []
    diff = len(a_binary) - len(b_binary)

    if diff != 0:
        c = a_binary if diff < 0 else b_binary
        for i in range(abs(diff)):
            c.appendleft(0)

    for i in range(len(a_binary)):
        result_num.append(int(a_binary[i] == 1 or b_binary[i] == 1))

    decimal_num = binary_to_decimal(result_num)
    return decimal_num


def xor_op_decimals(a: int, b: int) -> int:
    """
    If two bits are different - returns 1, else 0
    """
    a_binary, b_binary = decimal_to_binary(a), decimal_to_binary(b)
    result_num = []
    diff = len(a_binary) - len(b_binary)

    if diff != 0:
        s = a_binary if diff < 0 else b_binary
        for i in range(abs(diff)):
            s.appendleft(0)

    for i in range(len(a_binary)):
        result_num.append(int(not(a_binary[i] == b_binary[i])))

    decimal_num = binary_to_decimal(result_num)

    return decimal_num


def complimentary_op(a: int) -> int:
    return -a - 1


def left_shift(a: int, n: int) -> int:
    """
    Zeros are added to the binary tree on the left
    """
    a_binary = decimal_to_binary(a)
    for i in range(n):
        a_binary.append(0)

    decimal = binary_to_decimal(a_binary)

    return decimal


def right_shift(a: int, n: int) -> int:
    """
    First n bits from the binary a are being deleted
    """
    a_binary = decimal_to_binary(a)

    for i in range(n):
        a_binary.pop()

    decimal = binary_to_decimal(a_binary)
    return decimal


if __name__ == '__main__':
    print(right_shift(100, 3))