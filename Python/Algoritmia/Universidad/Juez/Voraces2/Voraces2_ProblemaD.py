n, c = map(int, input().strip().split())
comida = []
for i in range(n):
    a, t, v = map(str, input().strip().split())
    t = int(t)
    v = int(v)
    comida.append((v/t, v, t))
out = 0.0
comida.sort(reverse=True)
next = 0
while c > 0 and next < len(comida):
    if c >= comida[next][2]:
        out += comida[next][1]
        c -= comida[next][2]
    else:
        out += comida[next][1]  * (c / comida[next][2])
        c = 0
    next += 1
out = f"{out:.6f}" 
print(out)