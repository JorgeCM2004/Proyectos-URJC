#O(n!)
def dijkstra(edges, start, final, visited):
    if final in visited:
        return 9999999
    else:
        node_edges = list(filter(lambda x: x[2] == final, edges))
        if start == final:
            return 0
        else:
            out = []
            for i in node_edges:
                visited.append(i[2])
                out.append(dijkstra(edges, start,  i[1], visited) + i[0])
                visited.pop(-1)
            return min(out)

nodes, nedges = map(int, input().strip().split())
edges = []
for i in range(nedges):
    a, b, w = map(int, input().strip().split())
    edges.append((w, a, b))
s, f = map(int, input().strip().split())
print(dijkstra(edges, s, f, []))