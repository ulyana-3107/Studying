# Реализуйте линейную и хвостовую рекурсивные функции, получающие в качестве аргументов значение a, его положительное начальное
# приближение x0
#  и количество шагов n и возвращающие последнее приближение z = xn
#  после n-кратного применения (5.8). После этого определите их асимптотическую стоимость вычисления.


# def func2(a, x0):
#     return x0 - (x0**2 - a)/(2*x0)


# def func1(a, x0, n, func2):
#     if n == 0:
#         return x0
#     else:
#         return func1(a, func2(a, x0), n - 1, func2)


# def tail_rec(a, x0, n, func1, func2):
#     return func1(a, x0, n, func2)


def func(f1, f2, a, x0, n):
    if n == 0:
        return x0
    return func(f1, f2, a, x0 - f1(x0) / f2(x0), n - 1)


def func1(x0):
    pass


def func2(x0):
    pass


if __name__ == '__main__':
    x0, a, n = 1.4, 2, 5
    res1 = func(func1, func2, a, x0, n)
    print(res1)