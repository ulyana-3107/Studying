def ford_bellman(graph, source):
  distances = {vertex: float('inf') for vertex in graph}
  distances[source] = 0

  while True:
    updated = False

    for u, v, weight in graph.edges():
      if distances[u] + weight < distances[v]:
        distances[v] = distances[u] + weight
        updated = True

    if not updated:
      break

  return distances


graph = {
  'A': [('B', 10), ('C', 3)],
  'B': [('C', 1), ('D', 2)],
  'C': [('B', 4), ('D', 8), ('E', 2)],
  'D': [('E', 7)],
  'E': []
}
