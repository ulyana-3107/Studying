# True - if given integer is power of two, False - if no.


def power_of_two(n: int, p=2):
    if p > n:
        return False
    elif p == n:
        return True
    return power_of_two(n, 2 * p)


print(power_of_two(15))
