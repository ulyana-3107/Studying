def golden_triangle_norec(triangle: list) -> int:
    result = triangle[0]
    n = len(triangle)
    counter = 1
    for i in range(1, n):
        temp_arr = triangle[i]
        res = []
        for t in range(n - i):
            r = temp_arr[t] + max(result[t], result[t + 1])
            res.append(r)
        result = res
    return result[0]


print(golden_triangle_norec([[4, 5, 2, 6, 5], [2, 7, 4, 4], [8, 1, 0], [3, 8], [7]]))

