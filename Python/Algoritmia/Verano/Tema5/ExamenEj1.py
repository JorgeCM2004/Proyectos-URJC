def oneSubArrayAux(lista, mid, i, n):
    if lista[mid] == 1:
        aux = mid + 1
        contador = 1
        while aux <= n and lista[aux] == 1:
            contador += 1
            aux += 1
        aux = mid - 1
        while aux >= i and lista[aux] == 1:
            contador += 1
            aux -= 1
        return contador
    else:
        return 0
def oneSubArray(lista, i, n):
    if i == n:
        return lista[i]
    else:
        mid = (i + n) // 2
        r1 = oneSubArray(lista, i, mid)
        r2 = oneSubArray(lista, mid + 1, n)
        r3 = oneSubArrayAux(lista, mid, i, n)
        return max(r1, r2, r3)
l = [1, 0, 1, 0, 1, 0, 1, 0, 1]
print(oneSubArray(l, 0, len(l) - 1))