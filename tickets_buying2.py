from collections import deque


def count(comb, arr) -> int:
    counter, index = 0, 0
    for n in comb:
        counter += arr[index][n - 1]
        index += n
    return counter


def min_cost(n, curr_sum, comb, d, arr):
    if curr_sum == n:
        cost_ = count(comb, arr)
        if d[0] > cost_:
            d.pop()
            d.append(cost_)
        return
    if curr_sum > n:
        return
    for i in range(1, 4):
        min_cost(n, curr_sum + i, comb + [i], d, arr)
    return d[0]


arr = [[5, 10, 15], [2, 10, 15], [5, 5, 5], [20, 20, 1], [20, 1, 1]]
arr2 = [[3, 4, 5], [1, 1, 1]]

with open('tickets_input.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(str(len(arr2)) + '\n')
    for sub_arr in arr2:
        writer.write(' '.join([str(i) for i in sub_arr]) + '\n')

with open('tickets_input.txt', 'r', encoding='utf-8-sig') as reader:
    n_, arr_ = int(reader.readline().strip()), []
    for line in reader.readlines():
        arr_.append([int(i) for i in line.strip().split(' ')])

with open('tickets_output.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(str(min_cost(n_, 0, [], deque([float('inf')]), arr_)))


