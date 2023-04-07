# currency task
from collections import defaultdict

n = 3
matrix = [[1, -2, 3],
          [-3, 1, 2],
          [0.5, 0.5, 1]]
# Algorithm:
# 1) Инициализировать расстояния от источника до всех вершин как бесконечные, а расстояние до самого источника как 0,
# создать массив dist[] размером V со всеми бесконечными значениями, кроме dist[src], где src - исходная вершина.
# 2) На этом шаге вычисляются кратчайшие расстояния. Выполните следующие действия V - 1 раз, где V - количество вершин в
# данном графе
# 1. Выполнить следующие действия для каждого ребра u-v.
# 2. Если dist[v] > dist[u] + вес ребра uv, затем обновите dist[v].
# 3. dist[v] = dist[u] + вес ребра uv.
# 3) На этом шаге сообщается, есть ли отрицательный цикл веса на графе. Выполнить следующие действия для каждого ребра
# uv  1. Если dist[v] > dist[u] + вес ребра uv, то граф имеет цикл отрицательного веса
# Идея шага 3 заключается в том, что шаг 2 гарантирует кратчайшее расстояние, если граф не содержит отрицательного цикла
# Если мы переберем все ребра еще раз и получим более короткий путь для любой вершины, то найдем цикл с отрицательным ве
# сом.
src, v, edges, weights = 1, len(matrix), [], defaultdict(list)
for i in range(v):
    for j in range(v):
        if matrix[i][j] > 0 and i != j:
            edges.append((i + 1, j + 1))
for u, v in edges:
    weights[(u, v)].append(matrix[u - 1][v - 1])
dist = [[float('inf')] for _ in range(v + 1)]
dist[src - 1] = [0]
print(dist, edges, weights, sep='\n')
for i in range(v - 1):
    for u, v in edges:
        if dist[v - 1][-1] > dist[u - 1][-1] + weights[(u, v)][-1]:
            dist[v - 1][-1] = dist[u - 1][-1] + weights[(u, v)][-1]
for u, v in edges:
    if dist[v - 1][-1] > dist[u - 1][-1] + weights[(u, v)][-1]:
        print('Graph has negative cycle.')


