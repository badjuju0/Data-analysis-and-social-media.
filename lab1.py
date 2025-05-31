import heapq

def dijkstra_adj_matrix(graph, start):
    num_vertices = len(graph) #Считаем количество вершин (строк в матрице).
    distances = [float('inf')] * num_vertices #Массив distances хранит минимальные расстояния от начальной вершины до каждой другой.
    distances[start] = 0
    visited = [False] * num_vertices #Этот массив отслеживает, какие вершины мы уже обработали.

    for _ in range(num_vertices): #Проходим по всем вершинам.
        # Выбираем непосещённую вершину с минимальным расстоянием
        min_dist = float('inf')
        u = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                u = v

        if u == -1:  # оставшиеся вершины недостижимы
            break

        visited[u] = True #Отмечаем, что u мы обработали.

        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v]:
                new_dist = distances[u] + graph[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    #Обновляем расстояния для соседей вершины u, если через u можно дойти короче.

    return distances

def dijkstra_adj_list(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    queue = [(0, start)]
    #Словарь distances — минимальные расстояния. queue — приоритетная очередь, в которой храним (расстояние, вершина).

    while queue:
        current_distance, u = heapq.heappop(queue)
        #Берём вершину с наименьшим расстоянием из очереди.

        if current_distance > distances[u]:
            continue
        #Если уже нашли более короткий путь раньше — пропускаем.

        for neighbor, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                #Обновляем расстояния для соседей. Если нашли более короткий путь — добавляем соседа в очередь.
    return distances

adj_list = {
    0: [(1, 7), (2, 9), (5, 14)],
    1: [(0, 7), (2, 10), (3, 15)],
    2: [(0, 9), (1, 10), (3, 11), (5, 2)],
    3: [(1, 15), (2, 11), (4, 6)],
    4: [(3, 6), (5, 9)],
    5: [(0, 14), (2, 2), (4, 9)]
}

adj_matrix = [
    [0,  7,  9,  0,  0, 14],
    [7,  0, 10, 15, 0,  0],
    [9, 10, 0, 11, 0,  2],
    [0, 15,11, 0, 6,  0],
    [0,  0, 0, 6, 0,  9],
    [14, 0, 2, 0, 9,  0]
]

start_node = 0
#Указать adj_matrix или adj_list
print(dijkstra_adj_list(adj_list, start_node))



