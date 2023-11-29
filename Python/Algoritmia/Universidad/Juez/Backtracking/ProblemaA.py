def resolver_laberinto(laberinto: list, num: int, coords: tuple, solucion: bool) -> bool:
    if es_solucion():
        return True
    else:
        recorrer = 0
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while not solucion and recorrer > num:
            pass
    return solucion

def movimiento_factible() -> bool:
    pass

def es_solucion() -> bool:
    pass

num = int(input())
laberinto = []
ceros = 0
for i in range(num):
    fila = list(map(int, input().strip().split()))
    ceros += fila.count(0)
    laberinto.append(fila)

