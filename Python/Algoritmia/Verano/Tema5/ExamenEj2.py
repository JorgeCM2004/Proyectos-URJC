def construir(n, lista):
    lista.reverse()
    out = []
    for i in lista:
        out.append(n // i)
        n %= i
    out.reverse()
    if (n == 0 and out[0] < 2):
        return out
    else:
        return 'null'
v = int(input('Dame el numero de caras de la torre que quieres construir: '))
candidatos = [4, 6, 8, 12, 20]
print(construir(v, candidatos))