# data: n: number of vertices, edges: edges, weights: weights of edges
# need to find:  shortest paths for all vertices
# given: only list with all edge, weight tuples -> so we need to prepare params too
edges = [(1, 2, 8), (1, 3, 4), (1, 4, 2), (3, 4, 3), (2, 5, 5), (4, 6, 1), (5, 6, 3)]
edges2 = [(1, 2, 7), (1, 3, 9), (1, 6, 14), (2, 3, 10), (2, 4, 15), (3, 6, 2), (3, 4, 11), (4, 5, 6), (5, 6, 9)]
# algo: * first we create array marks and indicate all vertices marks as infinite instead of src mark which is 1 by
# defualt


def create_data(edges: list, src=1) -> tuple:
    n, marks, weights, graph = 0, {}, {}, dict()
    for e1, e2, w in edges:
        weights[(e1, e2)] = w
        if e1 > n:
            n = e1
        if e2 > n:
            n = e2
        if e1 not in graph:
            graph[e1] = {e2}
        else:
            graph[e1].add(e2)
        if e2 not in graph:
            graph[e2] = {e1}
        else:
            graph[e2].add(e1)
    for i in range(n):
        if i == src - 1:
            marks[i + 1] = 0
        else:
            marks[i + 1] = float('inf')
    if len(graph) < n:
        rest = n - len(graph)
        for i in range(n - rest + 1, n + 1):
            graph[i] = set()
    return n, marks, weights, graph


def dijkstra(edges: list) -> list:
    n, marks, weights, graph = create_data(edges, 1)
    visited, dict2 = set(), {}
    print(n, marks, weights)
    while len(visited) != n:
        v, mark_num = float('inf'), 0
        for k, v_ in marks.items():
            if v_ < v and k not in visited:
                v, mark_num = v_, k
        nbrs = graph[mark_num]
        for nb in nbrs:
            nb_mark = marks[nb]
            if (mark_num, nb) in weights:
                edge_mark = weights[(mark_num, nb)]
            else:
                edge_mark = weights[(nb, mark_num)]
            if v + edge_mark < nb_mark:
                marks[nb] = v + edge_mark
        visited.add(mark_num)
    return marks


print(dijkstra(edges2))