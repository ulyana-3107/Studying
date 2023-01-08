
def ford_bellman(edges, num_vertices, source, target):
  distances = [float('inf')] * num_vertices

  distances[source] = 0

  for i in range(num_vertices - 1):
    for (u, v, w) in edges:
      if distances[u] + w < distances[v]:
        distances[v] = distances[u] + w

  return distances[target]


edges = [(0, 1, 2), (1, 2, 3), (2, 3, 2), (3, 4, 1), (4, 5, 3), (5, 6, 1), (6, 7, 1), (7, 8, 1), (8, 9, 1), (9, 10, 1), (10, 0, 2)]

num_vertices = 11

source = 0
target = 10

shortest_path = ford_bellman(edges, num_vertices, source, target)

print(shortest_path)
