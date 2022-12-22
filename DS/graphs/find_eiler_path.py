def find_eulerian_tour(graph):
    stack = []
    tour = []

    stack.append(graph[0][0])

    while len(stack):
        v = stack[-1]
        degree = get_degree(v, graph)
        if degree == 0:
            stack.pop()
            tour.append(v)
        else:
            index, edge = get_edge_and_index(v, graph)
            graph.pop(index)
            stack.append(edge[1] if v == edge[0] else edge[0])
    return tour


def get_degree(v, graph):
    degree = 0
    for x, y in graph:
        if v in (x, y):
            degree += 1

    return degree

def get_edge_and_index(v, graph):
    edge = ()
    index = -1

    for i in range(len(graph)):
        if v in graph[i]:
            edge, index = graph[i], i
            break

    return index, edge

graph_ = [(0, 1), (1, 5), (1, 7), (4, 5),
         (4, 8), (1, 6), (3, 7), (5, 9),
         (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
# print(find_eulerian_tour(graph_))

def get_degree(v, graph):
    degr = 0
    for g in graph:
        if v in g:
            degr += 1
    return degr


# gr = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 2), (2, 1)]
# gr2 = [(1, 2), (1, 7), (2, 7), (2, 3), (3, 4), (4, 5), (5, 3), (2, 6), (6, 5), (3, 6), (6, 7), (7, 5)]
gr2 = [(1, 2), (2, 3), (3, 4), (4, 1)]
st = gr2[0][0]
res = []
stack = [st]
while stack:
    v = stack[-1]
    if get_degree(v, gr2) == 0:
        res.append(v)
        stack.pop()
    else:
        for g in gr2:
            if v == g[0]:
                edge = g
                break
        gr2.remove(edge)
        stack.append(edge[1])
print(res)


