def sumaPositivosAux(l, i, n):
    k = (i + n) // 2
    if i == n:
        if l[i] > 0:
            return l[i]
        else:
            return 0
    else:
        c1 = sumaPositivosAux(l, i, k)
        c2 = sumaPositivosAux(l, k + 1, n)
        return c1 + c2
def sumaPositivos(l):
    i = 0
    n = len(l) - 1
    return sumaPositivosAux(l, i, n)

print(sumaPositivos([-1, 0, 2, 3, 10, 12, -23, -14, -7]))