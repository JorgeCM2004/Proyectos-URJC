def encontrar_amantes(array: list, i: int, f: int, amante: int) -> int:
    k = (i + f) // 2
    if i == f and array[k] != amante:
        return -1
    elif array[k] == amante:
        return k
    else:
        if array[k] > amante:
            return encontrar_amantes(array, i, k - 1, amante)
        else:
            return encontrar_amantes(array, k + 1, f, amante)
numg1 = int(input()) - 1
g1 = list(map(int, input().strip().split()))
numg2 = int(input()) - 1
g2 = list(map(int, input().strip().split()))
num = int(input())
for i in range(num):
    a, b = map(int, input().strip().split())
    a = encontrar_amantes(g1, 0, numg1, a)
    b = encontrar_amantes(g2, 0, numg2, b)
    if a == -1 or b == -1:
        print("SIN DESTINO")
    else:
        print(a, b)