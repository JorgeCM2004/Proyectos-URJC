num = int(input())
t = 0
l = []
for i in range(num):
    a, b = map(int, input().strip().split())
    l.append(b)
l.sort()
c = 0
for i in range(num, 0, -1):
    t += l[c] * i
    c += 1
print(t)