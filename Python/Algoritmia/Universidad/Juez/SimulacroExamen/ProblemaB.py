def binary_search(i: int, f: int, searching: int) -> int:
    if i == f:
        return partidos[i][1]
    else:
        k = (i + f) // 2
        if partidos[k][0] >= searching:
            return binary_search(i, k, searching)
        else:
            return binary_search(k + 1, f, searching)

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    partidos = []
    for i in range(m):
        partidos.append([0, i])
    for i in range(m):
        p, v = map(int, input().strip().split())
        partidos[p][0] += v
    long = len(partidos)
    c = int(input().strip())
    partidos.sort()
    for i in range(1, long):
        partidos[i][0] += partidos[i - 1][0]
    long -= 1
    for i in range(c):
        recorrer = -1
        l = int(input().strip())
        print(binary_search(0, long, l))