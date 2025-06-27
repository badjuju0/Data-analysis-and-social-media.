import heapq

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        curr_dist, u = heapq.heappop(queue)
        if curr_dist > distances[u]:
            continue
        for v, weight in graph[u]:
            distance = curr_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(queue, (distance, v))

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print("Кратчайшие расстояния от вершины", start_vertex)
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")



