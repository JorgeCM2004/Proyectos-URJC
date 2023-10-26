def longMaxSubArrayOrdenadoAuxMid(l, k, i, n):
    contador = 1
    lista = [l[k]]
    while k + contador <= n and l[k] < l[k + contador]:
        lista.append(l[k + contador])
        contador += 1
    contador = 1
    while k - contador >= i and l[k] > l[k - contador]:
        lista.insert(0, l[k - contador])
        contador += 1
    return lista

def longMaxSubArrayOrdenadoAux(l, i, n):
    k = ((i + n)) // 2
    if i >= n :
        return [l[k]]
    else:
        m1 = longMaxSubArrayOrdenadoAux(l, i, k - 1)
        m2 = longMaxSubArrayOrdenadoAux(l, k + 1, n)
        m3 = longMaxSubArrayOrdenadoAuxMid(l, k, i, n)
        if len(m1) >= len(m2) and len(m1) >= len(m3):
            return m1
        elif len(m2) >= len(m1) and len(m2) >= len(m3):
            return m2
        else:
            return m3
    
def longMaxSubArrayOrdenado(l):
    i = 0
    n = len(l) - 1
    return longMaxSubArrayOrdenadoAux(l, i, n)

print(longMaxSubArrayOrdenado([2, 1, 1, 3, 2, 4, 7, 15, 1]))