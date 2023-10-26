#O(n * log(n))
import heapq
def dijkstra(graph, num_nodes, i, f):
    distances = [float('inf')] * nodes
    distances[i] = 0
    priority_queue = [(0, i)]
    while len(priority_queue) > 0:
        accumulated_weight, current_node = heapq.heappop(priority_queue)
        
    return distances[f]

graph = []
nodes, a = map(int, input().strip().split())
for i in range(a):
    node1, node2, w = map(int, input().strip().split())
    graph.append((node1 - 1, node2 - 1, w))
start, final = map(int, input().strip().split())
distance = dijkstra(graph, nodes, start - 1, final - 1)
print(distance)