def graph_weights(matrix: list) -> tuple:

    graph, weights, n = {}, {}, len(matrix)

    for i in range(n):
        graph[i] = set()
        for j in range(n):
            if matrix[i][j] and i != j:
                graph[i].add(j)
                weights[(i, j)] = matrix[i][j]

    return graph, weights


def shortest_path(src: int, graph: dict, weights: dict, n: int) -> dict:

    dist = {i: float("inf") for i in range(n)}
    dist[src] = 0

    for i in range(n - 1):
        for uv in weights.keys():
            u, v, w = uv[0], uv[1], weights[uv]
            u_dist, v_dist =  dist[u], dist[v]
            if v_dist > u_dist + w:
                dist[v] = u_dist + w

    for uv in weights.keys():
        u, v, w = uv[0], uv[1], weights[uv]
        if dist[v] > dist[u] + w:
            print('Negative cycle found!')


if __name__ == '__main__':

    matrix = [[0, 1, 2, -3, 0, 0],
              [1, 0, 0, 0, 0, 4],
              [2, 0, 0, 0, 0, 1],
              [3, 0, 0, 0, 2, 0],
              [0, 0, 0, 2, 0, 1],
              [0, 4, 1, 0, 1, 0]]

    curr1 = [[1, 2, 3],
             [0.4, 1, 2],
             [0.5, 0.5, 1]]

    curr2 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]

    gr, w = graph_weights(curr1)
    shortest_path(0, gr, w, 3)
