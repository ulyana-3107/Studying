from collections import deque

# Идея: данная матрица из (0, 1), или граф - разбивается на 1 (если весь граф связный) или несколько компонент в виде ребер (т.е. каждая компонента представлена в виде
# списка кортежей, а далее формируется список из этих компонент(или 1й компоненты), потом итерируясь по нему определяем, есть ли в компоненте хоть один цикл, если есть
# - значит людей не разделишь, а если нет - значит разделишь.

class Graph:
    """
    Class for graph representing.
    """
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def bfs(graph, start, n):
    """
    This function determines whether there are unvisited edges while search
    :param graph: list of lists where index of list - number of мукеуч, elements in list - connected vertexes
    :param start: start vertex for search
    :param n: number of vertexes
    :return: boolean, True - not all edges are visited (it means the graph has loop), False - unvisited edges not found
    (it means the graph does not have loop)
    """
    discovered = [False] * n
    discovered[start] = True
    q = deque()
    q.append((start, -1))
    while q:
        (v, parent) = q.popleft()
        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append((u, v))
            elif u != parent:
                return True
    return False


def has_loop(edges, n) -> bool:
    """
    This function determines whether graph has any loop or not
    :param edges: list of tuples (a, b), where a, b - number of vertexes connected
    :param n: number of vertexes in a graph
    :return: boolean, True - graph contains cycle, False - otherwise
    """
    graph = Graph(edges, n)
    if bfs(graph, 0, n):
        return True
    return False


def create_graph(matrix: list) -> dict:
    """
    This function creates dictionary k:v, where k - number of vertex, v - set of connected vertexes
    :param matrix: list of lists with 0's and 1's
    :return: dictionary
    """
    graph = {}
    for i in range(len(matrix)):
        graph[i] = set()
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and j != i:
                graph[i].add(j)
    return graph


def bfs2(gr: dict, start: int, visited: set) -> None:
    """
    This function - realisation of bfs algorithm
    :param gr: dictionary representing a graph
    :param start: number of start vertex, to start searching
    :param visited: set of already visited vertexes, empty in the beginning
    :return: None
    """
    fifo = deque([start])
    while fifo:
        v = fifo.popleft()
        visited.add(v)
        if len(gr[v]):
            for elem in gr[v]:
                if elem not in visited:
                    fifo.append(elem)


def function(matrix: list, start=0):
    """
    This function finds all the components in a graph.
    :param matrix: list of lists with 0's and 1's
    :param start: integer - number of vertex to start
    :return: list with sets of elements in each component
    """
    all, visited, n = [], set(), len(matrix)
    nodes, graph = [i for i in range(n)], create_graph(matrix)
    times = 0
    while len(visited) != n:
        vis2 = set([i for i in list(visited)])
        times += 1
        if times > 1:
            diff = set(nodes) - visited
            start = diff.pop()
        bfs2(graph, start, visited)
        diff = visited - vis2
        if len(diff):
            all.append(diff)
    return all


def function2(edges: list) -> tuple:
    """
    This function is additional - it converts the edges to right format
    :param edges: list of tuples
    :return: tuple (list, int) - list of new edges, number of vertexes
    """
    elems =set()
    for a, b in edges:
        elems.add(a)
        elems.add(b)
    lst = list(elems)
    lst.sort()
    indxs = {}
    for i in range(len(lst)):
        indxs[lst[i]] = i
    new_edges, n = [], len(lst)
    for a, b in edges:
        tup = (indxs[a], indxs[b])
        new_edges.append(tup)
    return new_edges, n


def possible(matrix: list) -> str:
    """
    This function determines whether it is possible to split people into two groups
    :param matrix: list of lists with 0's and 1's
    :return: string (Yes/No)
    """
    all = []
    edges = []
    sets = function(matrix)
    for s in sets:
        tuples = []
        for j in s:
            arr = matrix[j]
            for i in range(len(arr)):
                if arr[i] and i != j:
                    if (i, j) not in tuples:
                        tuples.append((j, i))
        edges.append(tuples)
    for e in edges:
        edges, n = function2(e)
        bool_ = has_loop(edges, n)
        all.append(bool_)
    res = not any(all)
    output = {True: 'Yes', False: 'No'}
    return output[res]


m1 = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]]  # 12  345
m2 = [[1, 0, 0, 1, 1], [0, 1, 0, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 1]]  # 12345
m3 = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]  # 1234
m4 = [[0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1],
      [0, 0, 0, 0, 1, 0]]


with open('acquaintances_inp.txt', 'w', encoding='utf-8-sig') as input_file:
    n, m = len(m1), m1
    tab = n//2
    input_file.write('  '*tab + str(n) + '\n')
    for arr in m:
        input_file.write(' '.join([str(num) for num in arr]) + '\n')


with open('acquaintances_inp.txt', 'r', encoding='utf-8-sig') as data_reader:
    data_reader.readline()
    matrix = []
    for line in data_reader.readlines():
        sub_arr = [int(num.strip()) for num in line.split(' ')]
        matrix.append(sub_arr)


with open('acquaintances_output.txt', 'w', encoding='utf-8-sig') as result_writer:
    result_writer.write(possible(matrix))


