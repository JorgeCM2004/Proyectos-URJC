def cerveza(l: list, i: int, nodes: int) -> list:
    distances = []
    for x in range(nodes):
        distances.append([float('inf'), None])
    distances[i][0] = 0
    not_visited = [True] * nodes
    while True in not_visited:
        neighbor = l[i]
        accum_weight = distances[i][0]
        for x in neighbor:
            if accum_weight + x[1] < distances[x[0]][0]:
                distances[x[0]][0] = accum_weight + x[1]
                distances[x[0]][1] = i
        not_visited[i] = False
        i = None
        for x in range(nodes):
            if (i == None or distances[x] < distances[i]) and not_visited[x]:
                i = x
    return distances

nodes, edges = map(int, input().strip().split())
graph = {}
for i in range(nodes):
    graph.update({i: []})
for i in range(edges):
    cerveza1, cerveza2, coste = map(int, input().strip().split())
    graph[cerveza1].append((cerveza2, coste))
    graph[cerveza2].append((cerveza1, coste))
i, f = map(int, input().strip().split())
out = cerveza(graph, i, nodes)
print(out[f][0])
recorrer = f
printear = []
while recorrer != None:
    printear.append(str(recorrer))
    recorrer = out[recorrer][1]
printear.reverse()
print(' '.join(printear))