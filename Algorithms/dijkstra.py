from __future__ import annotations
import heapq


def create_graph(matrix: list, n: int) -> dict:

    graph = {i: [] for i in range(len(matrix))}

    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j]:
                graph[i].append(j)

    return graph


def create_weights(matrix: list, n: int) -> dict:

    weights = {}

    for i in range(n):
        for j in range(n):
            if matrix[i][j] and i != j:
                weights[(i, j)] = matrix[i][j]

    return weights


def dijkstra_shortest_path(matrix: list, start: int) -> dict | list:

    n = len(matrix)
    graph, weights = create_graph(matrix, n), create_weights(matrix, n)
    start -= 1
    marks = [float('inf') for _ in range(len(matrix))]
    marks[start] = 0
    finished, node = set(), start

    while len(finished) != len(matrix):
        if len(finished):
            min_mark = float('inf'), 0
            for i in range(len(marks)):
                if marks[i] < min_mark[0] and i not in finished:
                    min_mark = marks[i], i
            node = min_mark[1]
        nbrs, costs = graph[node], []

        for nb in nbrs:
            if (node, nb) in weights:
                costs.append(weights[(node, nb)])
            else:
                costs.append(weights[(nb, node)])

        if len(costs) > 1:
            for i in range(len(costs)):
                m = costs[i], i
                for j in range(i + 1, len(costs)):
                    if costs[j] < m[0]:
                        m = costs[j], j
                if costs[i] > m[0]:
                    costs[i], costs[m[1]] = costs[m[1]], costs[i]
                    nbrs[i], nbrs[m[1]] = nbrs[m[1]], nbrs[i]

        for i in range(len(nbrs)):
            if marks[node] + costs[i] < marks[nbrs[i]]:
                marks[nbrs[i]] = marks[node] + costs[i]

        finished.add(node)

    return marks


if __name__ == '__main__':

    matrix = [[0, 7, 9, 0, 0, 14],
              [7, 0, 10, 15, 0, 0],
              [9, 10, 0, 11, 0, 2],
              [0, 15, 11, 0, 6, 0],
              [0, 0, 0, 6, 0, 9],
              [14, 0, 2, 0, 9, 0]]

    print(dijkstra_shortest_path(matrix, 1))
