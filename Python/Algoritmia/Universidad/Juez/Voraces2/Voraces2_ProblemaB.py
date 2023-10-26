n, m = map(int, input().strip().split())
casos = []
for i in range(n):
    p, d = map(int, input().strip().split())
    casos.append((d/p, d, p, i))
ganancia = 0
out = []
casos.sort(reverse=True)
next = 0
while m > 0 and next < len(casos):
    if casos[next][2] <= m:
        m -= casos[next][2] 
        ganancia += casos[next][1] 
    else:
        ganancia += round(casos[next][1]  * (m / casos[next][2]))
        m = 0
    out.append(casos[next][3])
    next += 1
out.sort()
for i in out:
    print(i, end= ' ')
print('\n' + str(ganancia))