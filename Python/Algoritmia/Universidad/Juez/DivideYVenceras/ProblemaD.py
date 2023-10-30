from copy import deepcopy
def matar_jugadores(array: list, i: int, f: int, buscar: int) -> int:
    k = (i + f) // 2
    if array[k] == buscar or i == f:
        out = array[k]
        if k + 1 < len(array) - 1 and array[k] < buscar:
            return k + 1
        return k
    else:
        if array[k] > buscar:
            return matar_jugadores(array, i, k - 1, buscar)
        else:
            return matar_jugadores(array, k + 1, f, buscar)

def minimo_encontradoX(array: list, index: int, buscando: int) -> int:
    copy_indexsup = index
    tamaño = len(array) - 1
    outofrangesup = False
    outofrangeinf = False
    while not outofrangesup and array[copy_indexsup] == 'X':
        copy_indexsup += 1
        if copy_indexsup > tamaño:
            outofrangesup = True
    copy_indexinf = index
    while not outofrangeinf and array[copy_indexinf] == 'X':
        copy_indexinf -= 1
        if copy_indexinf < 0:
            outofrangeinf = True
    if outofrangesup and outofrangeinf:
        return -1
    elif outofrangesup and not outofrangeinf:
        return copy_indexinf
    elif not outofrangesup and outofrangeinf:
        return copy_indexsup
    else:
        if array[copy_indexinf] - buscando <= array[copy_indexsup] - buscando:
            return copy_indexinf
        else:
            return copy_indexsup

num = int(input())
aux = ""
for i in range(num):
    aux += input() + " "
lista = list(map(int, aux.split()))
lista_modificable = deepcopy(lista)
eliminar = list(map(int, input().strip().split()))
for i in eliminar:
    index = matar_jugadores(lista, 0, num ** 2 - 1, i)
    if lista_modificable[index] == 'X':
        index = minimo_encontradoX(lista_modificable, index, i)
        if index != -1:
            lista_modificable[index] = 'X'
    else:
        lista_modificable[index] = 'X'
for i in range(num):
    for j in range(num):
        index = num * i + j
        print(lista_modificable[index], end= ' ')
    print()