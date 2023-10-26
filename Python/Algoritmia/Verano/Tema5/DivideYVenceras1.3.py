def elementoEspecialAux(l, i, n):
    k = (i + n) // 2
    if k == l[k]:
        return k
    else:
        if k > l[k]:
            return elementoEspecialAux(l, k + 1, n)
        else:
            return elementoEspecialAux(l, i, k - 1)
def elementoEspecial(l):
    i = 0
    n = len(l) - 1
    return elementoEspecialAux(l, i, n)

print(elementoEspecial([-10, -2, 0, 3, 7, 9, 19, 28, 30, 42, 55]))