from sortedcontainers import SortedDict


def create_input(collection, n, m, start_point=1) -> tuple:
    nbrs, weights = {}, {}  # O(1)
    for c in collection:  # O(E)
        v1, v2, w = c[0], c[1], c[2]  #O(1)
        if v1 not in nbrs:
            nbrs[v1] = set([v2])
        else:
            nbrs[v1].add(v2)
        if v2 not in nbrs:
            nbrs[v2] = set([v1])
        else:
            nbrs[v2].add(v1)
        # 8 - 11: O(1) + max(O(1), O(1)) - because set([v1]) , [v1] always length of 1 -> O(1)
        # 12 - 15: O(1) + max(O(1), O(1) -> O(1)
        # 7 - 15: O(1)
        if (v1, v2) in weights and (v2, v1) in weights:
            w1, w2 = None, None
            if weights[(v1, v2)] <= weights[(v2, v1)]:
                w1 = weights[(v1, v2)]
            else:
                w2 = weights[(v2, v1)]
            if w1:
                if w < w1:
                    weights[(v1, v2)] = w1
            else:
                if w < w2:
                    weights[(v2, v1)] = w2
            # 21 - 24: O(1) + max(O(1), O(1)) -> O(1)
            # 25 - 30: O(1) + max(O(1) + O(1), O(1) + O(1)) -> O(1)
            # 20 - 30: O(1)
        elif (v1, v2) in weights:
            if w < weights[(v1, v2)]:
                weights[(v1, v2)] = w
            # 35 - 36: O(1)
        else:
            weights[(v1, v2)] = w
        # 19 - 39: O(1)
    # 6 - 39:  O(E) * (O(1) + O(1)) -> O(E)
    marks_ = {i: float('inf') for i in range(1, n + 1)}  # O(N)
    marks_[start_point] = 0  # O(1)
    sd = SortedDict({float('inf'): i for i in range(1, n + 1)})  # O(N)
    sd[0] = start_point  # O(1)
    return nbrs, weights, marks_, sd
    # 4 - 46 (create_input function): O(E) + O(N) + O(1) + O(N) + O(1) -> O(N) + O(E) -> (N + E)


def dijkstra(collection, n, m, start_point=1) -> int:
    if m < 1:
        return 0
    nbrs, weights, marks_, sd = create_input(collection, n, m, start_point)  # O(N + E)
    visited = set()  # O(1)
    while len(visited) != n:  # O(N)
        for k, v in sd.items():
            curr_mark = v
            min_weight = k
            break
        # 56 - 59: O(1)
        nbs = [i for i in nbrs[curr_mark] if i not in visited]  # O(N - 1) -> O(N)
        temp = float('inf')  # O(1)
        for nb in nbs:  # O (N)
            nb_mark = marks_[nb]  # O(1)
            if (curr_mark, nb) in weights:  # O(1)
                edge_weight = weights[(curr_mark, nb)]  # O(1)
            else:
                edge_weight = weights[(nb, curr_mark)]  # o(1)
            # 64 - 68: o(1) + O(1) + max(O(1), O(1)) -> O(1)
            new_w = edge_weight + min_weight  # O(1)
            if new_w < nb_mark:
                marks_[nb] = new_w
                sd[new_w] = nb
            #  71 - 73: O(1) + o(1) + o(1) -> o(1)
            #   63 - 73: O(N) * O(1)
        visited.add(curr_mark)  # O(1)
        sd.pop(min_weight)  # O (1)
    return marks_[n]  # O(1)
    # 51 - 78: O(1) + O(N + E) + O(1) + O(N) * (O(1) + O(N) + O(1) + O(N)) -> O(N + E) + O(N**2) -> O(N**2)


edges = [(1, 2, 7), (1, 3, 9), (1, 6, 14), (2, 3, 10), (2, 4, 15), (3, 6, 2), (3, 4, 11), (5, 6, 9), (5, 4, 6)]
n, m, result = 6, 9, 11
edges1 = [(1, 2, 2), (2, 5, 5), (2, 3, 4), (1, 4, 1), (4, 3, 3), (3, 5, 1)]
n1, m1, result1 = 5, 6, 5
edges2 = [(1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 2, 5)]
n2, m2, result2 = 2, 6, 1
test = [(edges, n, m, result), (edges1, n1, m1, result1), (edges2, n2, m2, result2)]
for t in test:
    res = dijkstra(t[0], t[1], t[2])
    print(f'result: {res} -> {res==t[3]}')