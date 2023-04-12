def minimum_cost(axis: list) -> int:
    n = len(axis)
    if n <= 3:
        if n == 3:
            return axis[2] - axis[1] + (axis[1] - axis[0])
        else:
            return axis[1] - axis[0]
    else:
        rates = {1: axis[1] - axis[0], 2: axis[2] - axis[1] + axis[1] - axis[0]}
        for i in range(3, n):
            rates[i] = min(rates[i - 2], rates[i - 1]) + axis[i] - axis[i - 1]
        return round(rates[n - 1], 2)


axis_2 = [1, 2]  # 1
axis_1 = [1, 3, 8]  # 7
axis0 = [0, 2, 4, 10, 12]  # 6
axis1 = [11, 12, 13, 16, 17]  # 3
axis2 = [6.34, 6.82, 15.89, 24.58]  # 9.16
axis3 = [11, 12, 14, 16, 18]  # 5
axis4 = [11, 13, 14, 17, 21]  # 7


with open('nails_input.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(' '.join([str(num) for num in axis_1]))

with open('nails_input.txt', 'r', encoding='utf-8-sig') as reader:
    axis = []
    for line in reader.readlines():
        axis.extend([int(num) for num in line.strip().split(' ')])

result = minimum_cost(axis)

with open('nails_output.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(str(result))

