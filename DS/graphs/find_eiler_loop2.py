from __future__ import annotations


def create_graph(edges: list | tuple, n: int) -> dict:
    dict_res = {i: [] for i in range(1, n + 1)}  # O(1)
    for e in edges:  # O(E)
        e1, e2 = e  # O(1)
        dict_res[e1].append(e2)
        dict_res[e2].append(e1)
    return dict_res
# O(1) + O(E) -> O(E)


def loop_search(edges_: list, n_: int, start=1) -> list:
    lst, lifo, fifo = [], [start], []  # O(1)
    graph = create_graph(edges_, n_)  # O(E), where E - number of edges
    while len(lifo):  # O(E)
        v = lifo.pop()  # O(1)
        nbrs = graph[v]  # O(1)
        if len(nbrs):  # O(1)
            next_one = nbrs[0]
            lifo.extend([v, next_one])  # O(2) -> O(1)
            graph[v].remove(next_one)  # O(N)
            graph[next_one].remove(v)  # O(1)
        else:
            fifo.append(v)
    return fifo
# O(E*N)


n1, arr1 = 3, [(1, 2), (1, 3), (3, 2)]
n2, arr2 = 5, [(1, 2), (2, 5), (5, 3), (3, 4), (1, 4)]
n3, arr3 = 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 6), (6, 4), (2, 4), (6, 3), (3, 1), (6, 2)]
n4, arr4 = 4, [[1, 2], [2, 3], [3, 4], [4, 1]]
n, edges = n4, arr4


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

result = loop_search(arr, n)
print('Result is ready.')

with open('eiler_loop_output.txt', 'w', encoding='utf-8-sig') as output_writer:
    for r in result:
        output_writer.write(str(r) + ' ')
    print('Result is written.')
