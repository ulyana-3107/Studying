from collections import deque


def create_graph_from_matrix(matrix: list) -> dict:
    n = len(matrix)
    graph = {i + 1: set() for i in range(n)}

    for i in range(n):
        for j in range(n):
            if matrix[i][j] and i != j:
                graph[i + 1].add(j + 1)

    return graph


def can_divide(graph: dict) -> str:
    unwatched_elements = {i for i in graph.keys()}
    colors = {i: None for i in graph.keys()}
    start = unwatched_elements.pop()
    visited, stack = set(), deque([start])
    colors[start] = 1
    while len(visited) != len(graph):
        if not len(stack):
            elem = unwatched_elements.pop()
        else:
            elem = stack.popleft()
            unwatched_elements.discard(elem)
        visited.add(elem)
        clr = colors[elem]
        opposite_clr = 2 if clr == 1 else 1
        for nb in graph[elem]:
            if colors[nb] is not None:
                if colors[nb] == clr:
                    return 'No'
            else:
                colors[nb] = opposite_clr
                stack.append(nb)
    gr1, gr2 = set(), set()
    for k, v in colors.items():
        if v == 1:
            gr1.add(k)
        else:
            gr2.add(k)
    return 'Yes'


if __name__ == '__main__':

    matrix1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]  # NO
    matrix2 = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]]  # No
    matrix3 = [[1, 0, 0, 1, 1], [0, 1, 0, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 1]]  # Yes
    matrix4 = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]  # Yes
    matrix5 = [[1, 0, 1, 0, 0], [0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 0, 0, 1, 1], [0, 1, 0, 1, 0]]  # Yes
    matrix6 = [[1, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0],
               [1, 0, 0, 0, 0, 1]]  # Yes

    for i in range(1, 7):
        gr = create_graph_from_matrix(eval('matrix' + str(i)))
        print(can_divide(gr))



