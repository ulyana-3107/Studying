def create_data(edges: list, src: int) -> tuple:
    n_, weights_, edges_, marks_ = 0, {}, list(), {}
    for e1, e2, w in edges:
        edges_.append([e1, e2])
        if e1 > n_:
            n_ = e1
        if e2 > n_:
            n_ = e2
        weights_[(e1, e2)] = w
    for i in range(n_):
        if i == src - 1:
            marks_[i + 1] = 0
        else:
            marks_[i + 1] = float('inf')
    return n_, weights_, edges_, marks_


def bellman_ford(edges: list, src=1):
    n, weights, edges_, marks = create_data(edges, src)
    print(n, weights, edges_, marks, sep='\n')
    print(f'\n\n')
    visited = set()
    for i in range(n - 1):
        for e1, e2 in edges_:
            if marks[e1] != float('inf'):
                mark_1, mark_2 = marks[e1], marks[e2]
                edge_weight = weights[(e1, e2)]
                if mark_1 + edge_weight < mark_2:
                    marks[e2] = mark_1 + edge_weight
                    visited.add(e2)
            if len(visited) == n - 1:
                break
    print(f'marks: {marks}')
    for e1, e2 in edges_:
        mark_1, mark_2 = marks[e1], marks[e2]
        edge_weight = weights[(e1, e2)]
        if mark_1 + edge_weight < mark_2:
            print(f'Negative cycle found!')
            break


edges = [(1, 2, -1), (1, 3, 4), (2, 3, 3), (2, 4, 2), (4, 2, 1), (4, 3, 5), (5, 4, -3), (2, 5, 2)]
bellman_ford(edges)