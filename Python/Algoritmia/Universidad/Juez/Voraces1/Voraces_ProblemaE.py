a, b = map(int, input().strip().split())
tt = 0
l = []
for i in range(a):
    m, t = map(int, input().strip().split())
    l.append(t)
l.sort()
c = 0
for i in range(a, 0, -1):
    tt += l[c] * i
    c += 1
out = []
for i in range(b):
    tiempo = int(input())
    if tiempo >= tt:
        out.append("APROBADO")
    else:
        out.append("SUSPENSO")
for i in out:
    print(i)