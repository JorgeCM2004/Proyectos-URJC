def kruskal(nodes, edges):
    components = list(range(nodes))
    count = nodes
    mst = 0
    i = 0
    edges.sort()
    while count > 1 and len(edges) > i:
        w, u, v = edges[i]
        if components[u] != components[v]:
            count -= 1
            mst += w
            update_components(components, components[u], components[v])
        i += 1
    return mst

def update_components(components, oldID, newID):
    for i in range(len((components))):
        if components[i] == oldID:
            components[i] = newID

n, m = map(int, input().strip().split())
l = []
for i in range(m):
    u, v, e = map(int, input().strip().split())
    l.append((e, u, v))
print(kruskal(n, l) // 5 + 1)
