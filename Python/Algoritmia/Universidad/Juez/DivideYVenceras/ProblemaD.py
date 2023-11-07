def matar_jugadores(array: list, i: int, f: int, buscar: int) -> int:
    k = (i + f) // 2
    if array[k] == buscar or i >= f:
        if array[k] < buscar and k + 1 < len(array) - 1:
            return k + 1
        return k
    else:
        if array[k] > buscar:
            return matar_jugadores(array, i, k - 1, buscar)
        else:
            return matar_jugadores(array, k + 1, f, buscar)

num = int(input())
lista = []
for i in range(num):
    lista.extend(list(map(int, input().split())))
eliminar = list(map(int, input().strip().split()))
lista_aux = [0] * num ** 2
recorrer = 0
noacabado = True
while recorrer < len(eliminar) and noacabado:
    i = eliminar[recorrer]
    index = matar_jugadores(lista, 0, num ** 2 - 1, i)
    while index < len(lista_aux) and lista_aux[index] == 'X':
        index += 1
    if index > len(lista_aux) - 1:
        noacabado = False
    else:
        lista_aux[index] = 'X'
    recorrer += 1

for i in range(num):
    for j in range(num):
        index = num * i + j
        if lista_aux[index] == 0:
            print(lista[index], end= ' ')
        else:
            print(lista_aux[index], end= ' ')
    print()