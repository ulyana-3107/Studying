from __future__ import annotations

from collections import deque


def bfs(graph: dict | list, start=1) -> int:
    fifo, visited = deque([start]), set()
    if isinstance(graph, dict):
        while fifo:
            elem = fifo.popleft()
            visited.add(elem)
            elems = graph[elem]
            for el in elems:
                if el not in visited:
                    fifo.append(el)
    else:
        while fifo:
            elem = fifo.popleft()
            visited.add(elem)
            arr = graph[elem - 1]
            elems = [i + 1 for i in range(len(arr)) if arr[i] != 0]
            for el in elems:
                if el not in visited:
                    fifo.append(el)
    return len(visited)


def is_linked(graph: dict | list, n: int) -> bool:
    return bfs(graph) == n


def even_edge_degrees(graph: dict | list) -> bool:
    even = True
    if isinstance(graph, dict):
        for edge, nbrs in graph.items():
            if len(nbrs) % 2:
                even = False
                break
    else:
        for arr in graph:
            nbrs = [i for i in range(len(arr)) if arr[i] != 0]
            if len(nbrs) % 2:
                even = False
                break
    return even == bool(1)


def find_loop(graph: dict | list, n: int, start=0):
    _s, _c = [start], []
    while True:  # if N - number of vertices - O(N)
        v = _s[-1]
        if v in _s:
            if not len(graph[v]):
                if len(_s) == n:
                    break
                else:
                    _c.append(v)
            else:
                next = graph[v][0]
                graph[v].remove(next)
                graph[next].remove(v)
                _s.append(next)
        else:
            if graph[v]:
                next = graph[v][0]
                graph[v].remove(next)
                graph[next].remove(v)
                _s.append(next)
    return _c
# O(N)


gr_dict = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
gr_matrix = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
print(is_linked(gr_matrix, 4))
print(even_edge_degrees(gr_dict), even_edge_degrees(gr_matrix))
