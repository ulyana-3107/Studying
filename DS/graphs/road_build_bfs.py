from collections import deque

# N - количество вершин в графе
# M - количество дорог
# Q - количество разрушений дорог


def road_destroy(int_params: tuple, roads: list, destroy_numbers: list) -> str:
    n_, m_, q_ = int_params  # O(1)
    ways_dict = {t: [] for t in range(1, n_ + 1)}  # O(N)
    result = ''   # O(1)
    for w in roads:  # O(M)
        x, y = w[0], w[1]  # O(1)
        ways_dict[x].append(y)  # O(1)
        ways_dict[y].append(x)  # O(1)
    for road_num in destroy_numbers:  # O(Q)
        dest_way = m[road_num - 1]  # O(1)
        x, y = dest_way  # O(1)
        ways_dict[x].remove(y)  # O(len(dict[x])) - но тут всегда длина 2 так что O(1)
        ways_dict[y].remove(x)  # O(1)
        new_res = int(is_linked(ways_dict, n_, set()))  # O(1) (преобразование в int) + O(N**2) -> O(N**2)
        if new_res == 0:  # O(1)
            number = q_ - len(result)  # O(1)
            result += '0' * number  # O(1) + O(1) -> O(1)
            break
        result += str(new_res)  # O(1) + O(1) -> O(1)
    return result
# 9 - 11: O(1) + O(N) + O(1) -> O(N)
# 12 - 15: O(M) * (O(1) + O(1) + O(1)) -> O(M)
# 16 - 26: O(Q) * (O(1) + O(1) + O(1) + O(1) + O(N**2) + O(1) + (O(1) + O(1) + O(1)) -> O(Q) * O(N**2) -> O(N**2*Q)
# road_destroy function: O(N) + O(M) + O(N**2*Q) -> O(N**2*Q)


def is_linked(gr, n, visited, used=1) -> bool:
    bfs(gr, visited, 1)  # O(N)
    for i in range(1, n + 1):  # O(N)
        if i not in visited:  # O(1)
            used += 1  # O(1)
            bfs(gr, visited, i)  # O(N)
    if used == 1:  # O(1)
        return bool(1)  # O(1)
    else:
        return bool(0)  # O(1)
# 32 - 35: O(N) * (O(1) + O(N)) -> O(N**2)
# 36 - 39: O(1) + max(O(1), O(1)) -> O(1) + O(1) -> O(1)
# is_linked func: O(N) + O(N**2) + O(1) -> O(N**2)


def bfs(graph: dict, visited: set, start: int):
    stack = deque([start])  # O(1)
    while stack:  # O(N - 1) -> O(N)
        v = stack.popleft()  # O(1)
        visited.add(v)  # O(1)
        edges = graph[v]  # O(1)
        for edge in edges:  # O(N - 1) -> O(N)
            if edge not in visited:  # O(1)
                stack.append(edge)  # O(1)
# 44 - 50: O(N) * (O(1) + O(1) + O(1) + (O(N) * O(1) + O(1) -> O(N))) -> O(N)
# bfs function: O(1) + O(N) -> O(N)


n_, m_, q_ = 4, 6, 6
m = [[1, 2], [2, 3], [3, 4], [4, 1], [3, 1], [4, 2]]
q = [1, 6, 2, 5, 4, 3]
# n_, m_, q_ = 5, 5, 4
# m = [[1, 2], [2, 3], [2, 4], [1, 4], [5, 4]]
# q = [1, 5, 3, 4]
print(road_destroy((n_, m_, q_), m, q))


