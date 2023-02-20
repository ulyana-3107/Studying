from __future__ import annotations
from collections import deque
import random

# Comments: пока не меняла названия, мне пока кажется они правильные
# 1) row 66
# 2) row 31


def destroying(int_data: tuple, edges: list, roads_nums: list):
    n, m, q = int_data
    addr, comp_num = {i: i for i in range(1, n + 1)}, n
    components = {i: set([i]) for i in range(1, n + 1)}
    roads_nums = [roads_nums[i] for i in range(len(roads_nums) - 1, -1, -1)]
    if m == q:
        array = [comp_num]
    else:
        initial_roads_indxs = [ind for ind in range(1, len(edges) + 1) if ind not in roads_nums]
        initial_roads = [edges[i - 1] for i in initial_roads_indxs]
        data = build_roads(initial_roads, components, addr, comp_num, [])
        array = [data[0][-1]]
        components = data[1]
        addr = data[2]
        comp_num = data[3]
    roads = [edges[i - 1] for i in roads_nums]
    data = build_roads(roads, components, addr, comp_num, array)
    arr = data[0]
    return get_result(arr)


# * Эта функция просто строит дороги по тому-же принципу, что и в предыдущем задании, по ходу меняя состав компонент,
# количество компонент на данный момент (comp_num) и адреса вершин соответственно -> поэтому и возвращаются переданные
# параметры, но уже измененные.
# * В данной задаче эта функция может применяться 2/1 раз, в зависимости от того, равен ли параметр m (количество дорог)
# параметру q (количество разрушений): если они равны (строка 15): значит вызываем функцию 1 раз (т.к. до построения
# дорог которые потом разрушат дорог еще нет, но если m > q (строка 17) (разрушены не все дороги -> то на старте есть
# уже дороги, а значит нужно применить эту функцию (построить неразрушенные дороги) еще и перед тем, как строить разру
# шенные (в обратном порядке и вернуть измененные параметры, такие как компоненты, адреса, количество компонент на
# старте (чтоб было от чего отталкиваться) для их применения во втором вызове этой же функции.
def build_roads(roads: list, components: dict, addr: dict, comp_num: int, components_diff) -> tuple:
    for road in roads:
        t1, t2 = road
        a1, a2 = addr[t1], addr[t2]
        if a1 != a2:
            if comp_num > 1:
                comp_num -= 1
            l1, l2 = len(components[a1]), len(components[a2])
            if l2 > l1:
                elems = components[a1]
                for elem in elems:
                    addr[elem] = a2
                    components[a2].add(elem)
                addr[t1] = a2
                del components[a1]
            else:
                elems = components[a2]
                for elem in elems:
                    addr[elem] = a1
                    components[a1].add(elem)
                addr[t2] = a1
                del components[a2]
        components_diff.append(comp_num)
    return components_diff, components, addr, comp_num


# Эта функция превращает список из чисел (каждое число - это количество компонент связности) в итоговую строку(где 0 -
# это несвязный граф, а 1 - наоборот). Тут логика следующая: вместо разрушения дорог они строятся, только в обратном
# порядке -> по ходу построения определяется количество компонент связности после добавления новой дороги -> получаем
# этот массив -> дальше итерируемся по этому массиву но в обратном порядке, т.к. мы построили их в обратном порядке
def get_result(array: list) -> str:
    res, l = '', len(array) - 2
    while l != -1:
        if array[l] != 1:
            res += '0'*(l + 1)
            break
        else:
            res += str(array[l])
        l -= 1
    return res


# все функции ниже созданы лишь для доп. проверки правильности (поэтому закомментировала их)


# def create_graph(n: int, edges: list) -> dict:
#     graph = {i: set() for i in range(1, n + 1)}
#     for edge in edges:
#         v1, v2 = edge
#         graph[v1].add(v2)
#         graph[v2].add(v1)
#     return graph
#
#
# def bfs(graph: dict, start: int, visited: set) -> None | set:
#     fifo = deque([start])
#     while fifo:
#         v = fifo.popleft()
#         visited.add(v)
#         edges = graph[v]
#         if len(edges):
#             for e in edges:
#                 if e not in visited:
#                     fifo.append(e)
#     return visited
#
#
# def count_components(edges: list, n: int) -> int:
#     graph = create_graph(n, edges)
#     needed = set([i for i in range(1, n + 1)])
#     times = 1
#     vis = bfs(graph, 1, set())
#     diff = needed - vis
#     if len(diff):
#         while True:
#             s = random.choice(list(diff))
#             vis_ = bfs(graph, s, vis)
#             diff = needed - vis_
#             if not (len(diff)):
#                 return times + 1
#             else:
#                 times += 1
#     else:
#         return times


edges_, n_ = [[1, 5], [2, 3], [4, 2], [3, 1]], 5
edges2, n2 = [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 1]], 6
edges3, n3 = [[1, 2], [2, 3], [3, 4], [4, 1], [2, 4], [1, 3]], 6
edges4, n4 = [[1, 2], [2, 3], [3, 4], [4, 1], [2, 5]], 5
edges5 = [[1, 2], [2, 3], [3, 4], [4, 1], [3, 1], [4, 2]]
edges6 = [[1, 5], [1, 4], [1, 3], [1, 2]]
print(destroying((5, 4, 3), edges5, [1, 2, 3]))
