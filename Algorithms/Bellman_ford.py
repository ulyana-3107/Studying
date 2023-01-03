def prepare_data(n, edges) -> tuple:
    v_marks = {i: float('inf') for i in range(2, n + 1)}
    v_marks[1] = 0
    edge_weights = {(e[0], e[1]): e[2] for e in edges}
    edges = [(e[0], e[1]) for e in edges]
    return edges, v_marks, edge_weights


def dijkstra(n, edges) -> None:
    edges, v_marks, edge_weights = prepare_data(n, edges)
    for e in edges:
        if e in edge_weights:
            edge_ = e
        elif (e[1], e[0]) in edge_weights:
            edge_ = e
        cur_weight = v_marks[e[0]] + edge_weights[edge_]
        if cur_weight < v_marks[e[1]]:
            v_marks[e[1]] = cur_weight
    changed = False
    for e in edges:
        if e in edge_weights:
            edge_ = e
        elif (e[1], e[0]) in edge_weights:
            edge_ = e
        cur_weight = v_marks[e[0]] + edge_weights[edge_]
        if cur_weight < v_marks[e[1]]:
            v_marks[e[1]] = cur_weight
            changed = True
            break
    if changed:
        print('graph has negative-weighted edges')

    print(f'v_marks after calculating shortest path: {v_marks}')

edges = [(1, 2, 1), (1, 3, 2), (2, 4, 3), (3, 4, 3), (4, 5, 5), (4, 6, 2)]
dijkstra(6, edges)

