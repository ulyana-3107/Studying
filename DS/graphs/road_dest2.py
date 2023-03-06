from __future__ import annotations
from collections import deque
import random

# Добавила еще одну функцию(destroying2), которая для подсчета компонент связности использует bfs, а для изменения
# параметров components, addr - есть доп. функция так-же.


def destroying(int_data: tuple, edges: list, roads_nums: list):
    """
    This function builds roads in the reverse order of their destruction, determining the connectivity of the graph
    at each step
    :param int_data: tuple (n, m, q), where n - number of towns, m - number of roads, q - number of roads that will be
    destroyed
    :param edges: list with tuples (a, b), where a, b - connected towns
    :param roads_nums: list with digits, where each digit - number of town that will be destroyed
    :return: string with 0's and 1's, where 0 - graph is not linnked, 1 - graph is linked.
    """
    # Для оценки.
    # N - количество городов
    # M - количество дорог
    # Q - количество разрушений
    n, m, q = int_data  # O(1)
    addr, comp_num = {i: i for i in range(1, n + 1)}, n  # O(N) + O(1) -> O(N)
    components = {i: {i} for i in range(1, n + 1)}  # O(N)
    roads_nums = [roads_nums[i] for i in range(len(roads_nums) - 1, -1, -1)]  # O(Q)
    if m == q:  # O(1)
        array = [comp_num] # O(1)
    else:
        initial_roads_indxs = [ind for ind in range(1, len(edges) + 1) if ind not in roads_nums]  # O(M)
        initial_roads = [edges[i - 1] for i in initial_roads_indxs]  # O(M)
        data = build_roads(initial_roads, components, addr, comp_num, [])  # O(Q * M)
        array = [data[0][-1]]  # O(1)
        components = data[1]  # O(1)
        addr = data[2]  # O(1)
        comp_num = data[3]  # O(1)
    roads = [edges[i - 1] for i in roads_nums]  # O(Q)
    data = build_roads(roads, components, addr, comp_num, array)  # O(Q * M)
    arr = data[0]  # O(1)
    return get_result(arr)   # O(Q)
# O(N) + O(Q) + O(M) + O(Q * M) + O(Q) + O(Q * M) + O(Q) -> O(Q * M) + O(N) (тк неизвестно, чего больше(может быть и
# N - 15, Q - 3, M - 4, тогда 15 > 3*4. Поэтому O(QM + N).


def destroying2(int_data: tuple, edges: list, roads_nums: list) -> str:
    """
    This function is similar to the destroying function, with 2 differences: 1. Components at the start are calculated
    via bfs; 2. For changing components and addr parameters - new function created.
    :param int_data: tuple (n, m, q), where n - number of towns, m - number of roads, q - number of roads that will be
    destroyed
    :param edges: list with tuples (a, b), where a, b - connected towns
    :param roads_nums: list with digits, where each digit - number of town that will be destroyed
    :return: string with 0's and 1's, where 0 - graph is not linnked, 1 - graph is linked.
    """
    n, m, q = int_data  # O(1)
    addr, comp_num = {i: i for i in range(1, n + 1)}, n  # O(N) + O(1) -> O(N)
    components = {i: {i} for i in range(1, n + 1)}  # O(N)
    roads_nums = [roads_nums[i] for i in range(len(roads_nums) - 1, -1, -1)]  # O(Q)
    if m == q:  # O(1)
        array = [comp_num]  # O(1)
    else:
        initial_roads_nums = [i for i in range(len(edges)) if i + 1 not in roads_nums]  # O(M)
        initial_roads = [edges[i] for i in initial_roads_nums]  # O(M)
        components_at_start = count_components(n, initial_roads)  # O(M*N**2)
        change_params(initial_roads, components, addr, comp_num)  # O(M * N)
        array = [components_at_start]  # O(1)
    roads = [edges[i - 1] for i in roads_nums]  # O(Q)
    data = build_roads(roads, components, addr, comp_num, array)  # O(Q * M)
    arr = data[0]  # O(1)
    return get_result(arr)  # O(Q)
# O(N) + O(Q) + O(M) + O(M*N**2) + O(M * N) + O(Q) + O(Q*M) + O(Q) -> O(M*N**2).


def bfs(graph: dict, start: int, visited: set):
    """
    :param graph: dictionary k:v, where k - town, v - all the neighbours
    :param start: number of town from where the search starts
    :param visited: all the towns that the algorithm has visited
    :return: None
    """
    lifo = [start]  # O(1)
    while lifo:  # O(M)
        elem = lifo.pop()  # O(1)
        visited.add(elem)  # O(1)
        nbrs = graph[elem]  # O(1) -> O(1)
        if len(nbrs):  # O(1)
            for el in nbrs:  # O(N - 2) -> O(N)
                if el not in visited:  # O(1)
                    lifo.append(el)  # O(1)
# O(1) + O(M) * O(N) + O(1) * O(N) -> O(M*N) + O(N) -> O(M*N).


def create_graph(n, edges) -> dict:
    """
    :param n: number of towns in a graph
    :param edges: list with tuples (a, b), where a, b - 2 linked towns
    :return: dictionary representing a graph {k:v}, where k - town, v - all the neighbours
    """
    gr = {i: set() for i in range(1, n + 1)}  # O(N)
    for a, b in edges:  # O(M)
        gr[a].add(b)  # O(1)
        gr[b].add(a)  # O(1)
    return gr
# O(N) + O(M) * O(1) -> O(N) + O(M) но не известно, чего больше: дорог или городов поэтому O(N + M).


def count_components(n: int, edges: list) -> int:
    """
    :param n: number of towns
    :param edges: list of tuples (a, b) - where a, b - towns to be connected.
    :return: number of components in graph after building all the given roads.
    """
    towns = [i for i in range(1, n + 1)]  # O(N)
    graph = create_graph(n, edges)  # O(N + M)
    vis, times = set(), 0  # O(1) + O(1) -> O(1)
    while len(vis) != n:  # O(N)
        diff = set(towns) - vis  # O(N) + O(N) -> O(N)  так как len(vis) = N в худшем случае.
        start = diff.pop()  # O(1)
        bfs(graph, start, vis)  # O(M*N)
        times += 1  # O(1)
    return times
# O(N) + O(N + M) + O(N) * (O(N) + O(M*N))) -> O(N + M) + O(N) * O(M * N) -> O(M*N**2)


def change_params(edges: list, components: dict, addr: dict, comp_num: int) -> None:
    """
    In case when not all the roads are destroyed, this function is changing parameters components and addr.
    :param n: number of towns
    :param edges: edges to build
    :param components: dict k:v,  where k - number of component, v - set of towns in this component
    :param addr: dict k: v, where k - town number, v - number of component where the town is located
    :return: None
    """
    for t1, t2 in edges:  # O(M)
        a1, a2 = addr[t1], addr[t2]  # O(1)
        if a1 != a2:  # O(1)
            comp_num -= 1  # O(1)
            l1, l2 = len(components[a1]), len(components[a2])  # O(1)
            if l2 > l1:  # O(1)
                set_ = components[a1]  # O(1)
                for elem in set_:  # O(N - 1) - worst case
                    components[a2].add(elem)  # O(1)
                    addr[elem] = a2  # O(1)
                del components[a2]  # O(1)
            else:
                set_ = components[a2]  # O(1)
                for elem in set_:  # O(N - 1)
                    components[a1].add(elem)  # O(1)
                    addr[elem] = a1  # O(1)
                del components[a1]  # O(1)
# O(M) * O(N) -> O(M*N)


def build_roads(roads: list, components: dict, addr: dict, comp_num: int, components_diff) -> tuple:
    """
    :param roads: tuples (a, b) - where a, b - numbers of town that will be connected
    :param components: dictionary k:[**v], where k - number of component, **v - collection of town/towns in this
    component
    :param addr: dictionary k:v, where k - number of town, v - number of component where the town is located.
    :param comp_num: number of components to be chahged (e.g. in the beginning comp_num = 5, after connecting towns
    comp_num = 1)
    :param components_diff: list with n elements, where n - number of built roads, where each element - number of
    components after building road.
    :return: tuple with 4 elements: 1 - components_diff, 2 - components, 3 - addr, 4 - comp_num
    """
    for road in roads:  # O(Q)
        t1, t2 = road  # O(1)
        a1, a2 = addr[t1], addr[t2]  # O(1)
        if a1 != a2:  # O(1)
            if comp_num > 1:  # O(1)
                comp_num -= 1  # O(1)
            l1, l2 = len(components[a1]), len(components[a2])  # O(1) + O(1) -> O(1)
            if l2 > l1:  # O(1)
                elems = components[a1]  # O(1)
                for elem in elems:  # O(N-1) -> O(N)
                    addr[elem] = a2  # O(1)
                    components[a2].add(elem)  # O(1)
                addr[t1] = a2  # O(1)
                del components[a1]  # O(1)
            else:
                elems = components[a2]  # O(1)
                for elem in elems:  # O(N-1) -> O(N)
                    addr[elem] = a1  # O(1)
                    components[a1].add(elem)  # O(1)
                addr[t2] = a1  # O(1)
                del components[a2]  # O(1)
        components_diff.append(comp_num)  # O(1)
    return components_diff, components, addr, comp_num
# O(Q) * O(N) -> O(Q*M)


def get_result(array: list) -> str:
    """
    This function converts an array to the result string
    :param array: list with digits, each digit - number of components after building(destroying) one road
    :return: string with 0's and 1's of n length, where n - number of destroyed roads, 0 - graph is not linked,
    1 - graph is linked.
    """
    res, l = '', len(array) - 2  # O(Q)
    while l != -1:  # O(Q) - worst case
        if array[l] != 1:  # O(1)
            res += '0'*(l + 1)  # O(1)
            break
        else:
            res += str(array[l])  # O(1)
        l -= 1  # O(1)
    return res
# O(Q) + O(Q) * (O(1) + max(O(1), O(1)) + O(1)) -> O(Q) + O(Q) -> O(Q)


edges_, n_ = [[1, 5], [2, 3], [4, 2], [3, 1]], 5
edges2, n2 = [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 1]], 6
edges3, n3 = [[1, 2], [2, 3], [3, 4], [4, 1], [2, 4], [1, 3]], 6
edges4, n4 = [[1, 2], [2, 3], [3, 4], [4, 1], [2, 5]], 5
edges5 = [[1, 2], [2, 3], [3, 4], [4, 1], [3, 1], [4, 2]]
edges6 = [[1, 5], [1, 4], [1, 3], [1, 2]]
