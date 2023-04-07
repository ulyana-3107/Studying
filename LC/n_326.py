# Given an integer n, return  True, if it is a power of three, otherwise return  False.


def if_power_of_three(n: int, p: int = 3) -> bool:
    if n == 1:
        return True
    if p == n:
        return True
    elif p > n:
        return False
    else:
        return if_power_of_three(n, 3 * p)


def if_power_of_three2(n: int) -> bool:
    if n == 1:
        return True
    start = 3
    while True:
        if n > start:
            start *= 3
        elif n < start:
            return False
        else:
            return True


numbers = [3, 1, 2, 9, 7, 27]
for number in numbers:
    print(number, if_power_of_three(number), if_power_of_three2(number), sep='--')