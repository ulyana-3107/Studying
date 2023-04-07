def count(line: str) -> str:
    arr, n, l = [], len(line), ''
    for i in range(len(line)):  # O(L)
        l += line[i]
        if i != len(line) - 1:
            if line[i + 1] != l[-1]:
                arr.append(l)
                l = ''
        else:
            arr.append(l)
    result_line = ''
    for num in arr:
        result_line += str(len(num))
        result_line += num[0]
    return result_line


def count_and_say(n: int, curr_n=1, string='1'):
    if curr_n == n:
        print(string)
    else:
        string = count(string)
        count_and_say(n, curr_n + 1, string)


# Сложность - O(n) - количество вызовов функции count_and_say равно n - 1.


for i in range(1, 10):
    print(f'i: {i}')
    count_and_say(i)