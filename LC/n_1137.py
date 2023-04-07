def tribonacci_loop(n: int) -> int:
    arr = [0, 1, 1]
    if n in range(len(arr)):
        return arr[n]
    else:
        a, b, c = arr
        for i in range(n - len(arr) + 1):
            a, b, c = b, c, a + b + c
        return c


cases = [0, 1, 2, 3, 4]
for c in cases:
    print(tribonacci_loop(c))
