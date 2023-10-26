#O(n^2)
def dijkstra(graph, nodes, start, final):
    vertices = list(range(nodes))
    distances = [float('inf')] * nodes
    distances[start] = 0
    not_visited = [True] * nodes
    while True:
        min_vertex = None
        for vertex in vertices:
            if (min_vertex is None or distances[vertex] < distances[min_vertex]) and not_visited[vertex]:
                min_vertex = vertex
        if min_vertex is None:
            return distances[final]
        not_visited[min_vertex] = False
        current_distance = distances[min_vertex]
        current_edges = list(filter(lambda x: x[0] == min_vertex, graph))
        for _, neighbor, weight in current_edges:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

graph = []
nodes, a = map(int, input().strip().split())
for i in range(a):
    node1, node2, w = map(int, input().strip().split())
    graph.append((node1 - 1, node2 - 1, w))
start, final = map(int, input().strip().split())
distance = dijkstra(graph, nodes, start - 1, final - 1)
print(distance)