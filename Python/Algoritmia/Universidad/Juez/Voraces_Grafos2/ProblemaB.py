def cerveza(l: list, i: int, nodes: int) -> list:
    distances = []
    for x in range(nodes):
        distances.append([float('inf'), None])
    distances[i][0] = 0
    not_visited = [True] * nodes
    while True in not_visited:
        neighbor = list(filter(lambda x: x[1] == i or x[2] == i, l))
        accum_weight = distances[i][0]
        for x in neighbor:
            if x[1] == i:
                if accum_weight + x[0] < distances[x[2]][0]:
                    distances[x[2]][0] = accum_weight + x[0]
                    distances[x[2]][1] = x[1]
            else:
                if accum_weight + x[0] < distances[x[1]][0]:
                    distances[x[1]][0] = accum_weight + x[0]
                    distances[x[1]][1] = x[2]
        not_visited[i] = False
        i = None
        for x in range(nodes):
            if (i == None or distances[x] < distances[i]) and not_visited[x]:
                i = x
    return distances

nodes, edges = map(int, input().strip().split())
graph = []
for i in range(edges):
    cerveza1, cerveza2, coste = map(int, input().strip().split())
    graph.append((coste, cerveza1, cerveza2))
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