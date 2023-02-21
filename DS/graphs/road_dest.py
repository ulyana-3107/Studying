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
    n, m, q = int_data
    addr, comp_num = {i: i for i in range(1, n + 1)}, n
    components = {i: {i} for i in range(1, n + 1)}
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
    n, m, q = int_data
    addr, comp_num = {i: i for i in range(1, n + 1)}, n
    components = {i: {i} for i in range(1, n + 1)}
    roads_nums = [roads_nums[i] for i in range(len(roads_nums) - 1, -1, -1)]
    if m == q:
        array = [comp_num]
    else:
        initial_roads_nums = [i for i in range(len(edges)) if i + 1 not in roads_nums]
        initial_roads = [edges[i] for i in initial_roads_nums]
        components_at_start = count_components(n, initial_roads)
        change_params(initial_roads, components, addr, comp_num)
        array = [components_at_start]
    roads = [edges[i - 1] for i in roads_nums]
    data = build_roads(roads, components, addr, comp_num, array)
    arr = data[0]
    return get_result(arr)


def bfs(graph: dict, start: int, visited: set):
    """
    :param graph: dictionary k:v, where k - town, v - all the neighbours
    :param start: number of town from where the search starts
    :param visited: all the towns that the algorithm has visited
    :return: None
    """
    lifo = [start]
    while lifo:
        elem = lifo.pop()
        visited.add(elem)
        nbrs = graph[elem]
        if len(nbrs):
            for el in nbrs:
                if el not in visited:
                    lifo.append(el)


def create_graph(n, edges) -> dict:
    """
    :param n: number of towns in a graph
    :param edges: list with tuples (a, b), where a, b - 2 linked towns
    :return: dictionary representing a graph {k:v}, where k - town, v - all the neighbours
    """
    gr = {i: set() for i in range(1, n + 1)}
    for a, b in edges:
        gr[a].add(b)
        gr[b].add(a)
    return gr


def count_components(n: int, edges: list) -> int:
    """
    :param n: number of towns
    :param edges: list of tuples (a, b) - where a, b - towns to be connected.
    :return: number of components in graph after building all the given roads.
    """
    towns = [i for i in range(1, n + 1)]
    graph = create_graph(n, edges)
    vis, times = set(), 0
    while len(vis) != n:
        diff = set(towns) - vis
        start = diff.pop()
        bfs(graph, start, vis)
        times += 1
    return times


def change_params(edges: list, components: dict, addr: dict, comp_num: int) -> None:
    """
    In case when not all the roads are destroyed, this function is changing parameters components and addr.
    :param n: number of towns
    :param edges: edges to build
    :param components: dict k:v,  where k - number of component, v - set of towns in this component
    :param addr: dict k: v, where k - town number, v - number of component where the town is located
    :return: None
    """
    for t1, t2 in edges:
        a1, a2 = addr[t1], addr[t2]
        if a1 != a2:
            comp_num -= 1
            l1, l2 = len(components[a1]), len(components[a2])
            if l2 > l1:
                set_ = components[a1]
                for elem in set_:
                    components[a2].add(elem)
                    addr[elem] = a2
                del components[a2]
            else:
                set_ = components[a2]
                for elem in set_:
                    components[a1].add(elem)
                    addr[elem] = a1
                del components[a1]


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


def get_result(array: list) -> str:
    """
    This function converts an array to the result string
    :param array: list with digits, each digit - number of components after building(destroying) one road
    :return: string with 0's and 1's of n length, where n - number of destroyed roads, 0 - graph is not linked,
    1 - graph is linked.
    """
    res, l = '', len(array) - 2
    while l != -1:
        if array[l] != 1:
            res += '0'*(l + 1)
            break
        else:
            res += str(array[l])
        l -= 1
    return res


edges_, n_ = [[1, 5], [2, 3], [4, 2], [3, 1]], 5
edges2, n2 = [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 1]], 6
edges3, n3 = [[1, 2], [2, 3], [3, 4], [4, 1], [2, 4], [1, 3]], 6
edges4, n4 = [[1, 2], [2, 3], [3, 4], [4, 1], [2, 5]], 5
edges5 = [[1, 2], [2, 3], [3, 4], [4, 1], [3, 1], [4, 2]]
edges6 = [[1, 5], [1, 4], [1, 3], [1, 2]]
