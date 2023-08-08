# Реализуйте линейную и хвостовую рекурсивные функции, получающие в качестве аргументов значение a, его положительное начальное
# приближение x0
#  и количество шагов n и возвращающие последнее приближение z = xn
#  после n-кратного применения (5.8). После этого определите их асимптотическую стоимость вычисления.


def func2(a, x0):
    return x0 - (x0**2 - a)/(2*x0)


def func1(a, x0, n, func2):
    if n == 0:
        return x0
    else:
        return func1(a, func2(a, x0), n - 1, func2)


def tail_rec(a, x0, n, func1, func2):
    return func1(a, x0, n, func2)

# def linear_rec(a, x0, n, xn_1=None) -> float:
#     if n == 0:
#         return xn_1
#
#     else:
#
#         if xn_1 is None:
#             xn_1 = x0
#
#         xn = xn_1 - (xn_1 ** 2 - a)/(2*xn_1)
#
#         return linear_rec(a, x0, n - 1, xn)


if __name__ == '__main__':
    x0, a, n = 1.4, 2, 5
    res1 = tail_rec(a, x0, n, func1, func2)
    print(res1)