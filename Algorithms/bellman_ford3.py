def ford_bellman(graph, source):
    distances = [float('inf')] * len(graph)
    distances[source] = 0

    for _ in range(len(graph) - 1):
        for u in range(len(graph)):
            for v in range(len(graph[u])):
                if distances[u] != float('inf') and distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]

    for u in range(len(graph)):
        for v in range(len(graph[u])):
            if distances[u] != float('inf') and distances[u] + graph[u][v] < distances[v]:
                print("Graph contains negative-weight cycle")
                return

    print(f"Vertex   Distance from source")
    for i in range(len(distances)):
        print(f"{i} \t\t {distances[i]}")


graph = [[0, -1, 4, float('inf'), float('inf')],
         [float('inf'), 0, 3, 2, 2],
         [float('inf'), float('inf'), 0, float('inf'), float('inf')],
         [float('inf'), 1, 5, 0, float('inf')],
         [float('inf'), float('inf'), float('inf'), -3, 0]]

source = 0
ford_bellman(graph, source)
