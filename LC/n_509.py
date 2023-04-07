#  Дается номер порядковый из последовательности фибоначи, нужно выдать число
# 0 1 1 2 3 5 8 13 21 34 55 89

def fib_1(n: int):
    d = {0: 1, 1: 2}
    if n in d:
        return d[n]
    else:
        i = 1
        a, b = 0, 1
        while b != n:
            a, b = b, a + b
            i += 1
        return i


# Но теперь нужно реализовать это через рекурсию
def fib_2(n: int, a=0, b=1, i=1):
    if i == 1 and n in (a, b):
        return n + 1
    if b == n:
        return i
    else:
        return fib_2(n, b, a + b, i + 1)


# def fib_3(n: int) -> int:
#     if n in range(2):
#         return n
#     else:
#         return fib_3(n - 1) + fib_3(n - 2)


lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elem in lst:
    print(elem, fib_1(elem), fib_2(elem), sep='---')




