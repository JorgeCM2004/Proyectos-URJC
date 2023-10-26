def prim(edges):
    out = 0
    visitado = []
    edges.sort()
    out += edges[0][0]
    visitado.append(edges[0][1], edges[0][2])
    for i in len(edges):
        if (i[1] not in visitado and i[2] in visitado) or (i[2] not in visitado and i[1] in visitado):
            visitado.append(i[1], i[2])
            out += i[0]
    return out

n, m = map(int, input().strip().split())
l = []
for i in range(m):
    u, v, e = map(int, input().strip().split())
    l.append((e, u, v))
mst = prim(l)
print(mst)