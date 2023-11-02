def matar_jugadores(array: list, array_aux: list, i: int, f: int, buscar: int) -> int:
    k = (i + f) // 2
    if array[k] == buscar or i >= f:
        if array_aux[k] == 'X' or array[k] < buscar:
            return k + 1
        return k
    else:
        if array[k] > buscar:
            return matar_jugadores(array, array_aux, i, k - 1, buscar)
        else:
            return matar_jugadores(array, array_aux, k + 1, f, buscar)

num = int(input())
lista = []
for i in range(num):
    lista.extend(list(map(int, input().split())))
eliminar = list(map(int, input().strip().split()))
lista_aux = [0] * num ** 2
index_ant = 0
for i in eliminar:
    index = matar_jugadores(lista, index_ant, num ** 2 - 1, i)
    index_ant = index + 1
    lista[index] = 'X'

for i in range(num):
    for j in range(num):
        index = num * i + j
        if lista_aux[index] == 0:
            print(lista[index], end= ' ')
        else:
            print(lista_aux[index], end= ' ')
    print()