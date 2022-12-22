from collections.abc import Iterable
from collections import deque


def graph_even_odd(data: Iterable) -> tuple:
    n, edges = data
    even_odd, graph = {}, {v: None for v in range(1, n + 1)}
    # while iterating through edges collection graph is being created
    # and dict, where key is vert number, value - degree
    for edge in edges:
        for v in edge:
            if v not in even_odd:
                even_odd[v] = 1
            else:
                even_odd[v] += 1
        a, b = edge
        if graph[a]:
            graph[a].add(b)
        else:
            graph[a] = {b}
    return n, even_odd, graph


def bfs(graph: dict, start: int) -> set:
    visited, queue = set(), deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        visited.add(v)
        if graph[v]:
            for v_ in graph[v]:
                if v_ not in visited:
                    queue.append(v_)
    return visited


data_ = [4, [(1, 2), (3, 1), (2, 3)]]
gr = graph_even_odd(data_)


# Before starting to search for euler loop we need to check if that loop is present (-> graph is euler graph)
def has_loop(data: Iterable) -> bool:
    condition1, condition2 = True, True
    n, even_odd, graph = graph_even_odd(data)
    for v in even_odd.values():
        if v % 2:
            condition1 = False
            break
    c, visited_edges, accessible = 0, {}, set([i for i in range(1, n + 1)])
    while accessible:
        c += 1
        start = accessible.pop()
        accessible.add(start)
        component = bfs(graph, start)
        accessible = accessible ^ component
        if len(component) > 1 and c > 1:
            condition2 = False
            break
    if condition1 and condition2:
        return True
    else:
        if condition1:
            print('Not all graph vertices have an even degree')
            return False
        elif condition2:
            print('Number of connected components with edges must not exceed one')
        else:
            print('None of conditions is met')


has_loop(data_)






