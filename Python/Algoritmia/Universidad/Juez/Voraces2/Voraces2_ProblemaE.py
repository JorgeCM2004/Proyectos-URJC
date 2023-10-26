n, k = map(int, input().strip().split())
participantes = []
for i in range(n):
    nombre, edad = map(str, input().strip().split())
    participantes.append((int(edad), nombre))
participantes.sort()
out = ''
for i in range(k):
    out += participantes[i][1] + ' '
print(out[:-1])
out = ''
for i in range(k, len(participantes)):
    out += participantes[i][1] + ' '
print(out[:-1])