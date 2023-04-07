# Given an integer n, return True if it is a power of four, otherwise return False.


def if_power_of_four(n: int, p: int = 4) -> bool:
    if n < p:
        return if_power_of_four(n, 4 * p)
    elif n > p:
        return False
    else:
        return True


def if_power_of_four2(n: int) -> bool:
    if n in (1, 4):
        return True
    else:
        mult = 4
        while True:
            if n > mult:
                mult *= 4
            elif n < mult:
                return False
            else:
                return True


numbers = [1, 2, 3, 4, 6, 16, 64, 88, 256]
for num in numbers:
    print(num, if_power_of_four2(num), sep='--')