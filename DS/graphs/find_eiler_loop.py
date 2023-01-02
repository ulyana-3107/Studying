from collections import deque


def loop_search(arr) -> list:
    lifo, fifo = deque(), list()
    lifo.append(1)
    while lifo:
        v, edge_ = lifo.pop(), None
        for edge in arr:
            if v in edge:
                edge_ = edge
                break
        if edge_:
            arr.remove(edge_)
            if edge_[0] != v:
                edge_ = [edge_[1], edge_[0]]
            lifo.append(edge_[1])
            fifo.append(v)
        else:
            fifo.append(v)
    return fifo


n1, arr1 = 3, [(1, 2), (1, 3), (3, 2)]
n2, arr2 = 5, [(1, 2), (2, 5), (5, 3), (3, 4), (1, 4)]
n3, arr3 = 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 6), (6, 4), (2, 4), (6, 3), (3, 1), (6, 2)]
n, edges = n3, arr3


with open('eiler_loop_input.txt', 'w', encoding='utf-8-sig') as input_writer:
    input_writer.write(str(n) + '\n')
    for e in edges:
        input_writer.write(' '.join([str(i) for i in e]) + '\n')
    print('Input is wriiten.')

with open('eiler_loop_input.txt', 'r', encoding='utf-8-sig') as input_reader:
    n, arr = int(input_reader.readline().strip()), []
    for line in input_reader.readlines():
        arr.append([int(i) for i in line.strip().split(' ')])
    print('Input is read.')

result = loop_search(arr)
print('Result is ready.')

with open('eiler_loop_output.txt', 'w', encoding='utf-8-sig') as output_writer:
    for r in result:
        output_writer.write(str(r) + ' ')
    print('Result is written.')
