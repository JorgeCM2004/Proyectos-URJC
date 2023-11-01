def matar_jugadores(array: list, i: int, f: int, buscar: int) -> int:
    k = (i + f) // 2
    if array[k] == buscar or i == f:
        if k + 1 < len(array) - 1 and array[k] < buscar:
            return k + 1
        return k
    else:
        if array[k] > buscar:
            return matar_jugadores(array, i, k, buscar)
        else:
            return matar_jugadores(array, k + 1, f, buscar)

num = int(input())
aux = ""
for i in range(num):
    aux += input() + " "
lista = list(map(int, aux.split()))
eliminar = list(map(int, input().strip().split()))
index_ant = 0
for i in eliminar:
    index = matar_jugadores(lista, index_ant, num ** 2 - 1, i)
    index_ant = index + 1
    lista[index] = 'X'

for i in range(num):
    for j in range(num):
        index = num * i + j
        print(lista[index], end= ' ')
    print()