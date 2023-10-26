n, m = map(int, input().strip().split())
cartas = []
for i in range(n):
    c, r, b = map(str, input().strip().split())
    r = int(r)
    b = int(b)
    cartas.append((b/r, c, r))
out = ''
cartas.sort(reverse=True)
next = 0
while m > 0 and next < len(cartas):
    out += cartas[next][1] + ' '
    m -= cartas[next][2]
    next += 1
print(out[:-1])