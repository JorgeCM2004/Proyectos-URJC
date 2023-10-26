#No reduce nada.
def suma_medio(array, i, j, k):
    lista_sumas = []
    recorrer = k + 1
    sumas = 0
    while recorrer <= j:
        sumas += array[recorrer]
        lista_sumas.append(sumas)
        recorrer += 1
    sumas = max(lista_sumas)
    lista_sumas = []
    recorrer = k
    while recorrer >= i:
        sumas += array[recorrer]
        lista_sumas.append(sumas)
        recorrer -= 1
    return max(lista_sumas)

def sumas_parciales(array: list, i: int, j: int):
    if i > j:
        return 0
    if i == j:
        return array[i]
    else:
        k = (i + j) // 2
        sum1 = sumas_parciales(array, i, k)
        sum2 = sumas_parciales(array, k + 1, j)
        sum3 = suma_medio(array, i, j, k)
        return max(sum1, sum2, sum3)
lista = [1, 1, 1, -4, 1, 1, 1, 1, 1, 1]
ini = 0
fin = len(lista) - 1
print(sumas_parciales(lista, ini, fin))
