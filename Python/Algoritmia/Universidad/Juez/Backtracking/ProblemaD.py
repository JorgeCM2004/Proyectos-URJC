def defender_ciudad(mapa: list, lim0: int, lim1: int, coords: tuple, solucion: bool, d: int, enemigos: int) -> bool:
    if es_solucion(enemigos, coords, mapa):
        return True
    else:
        recorrer = 0
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while not solucion and recorrer < 4 and d > 0:
            movimiento = movimientos[recorrer]
            if movimiento_factible(mapa, (coords[0] + movimiento[0], coords[1] + movimiento[1]), lim0, lim1):
                if mapa[coords[0]][coords[1]] == 0:
                    mapa[coords[0]][coords[1]] = -1
                    solucion = defender_ciudad(mapa, lim0, lim1, (coords[0] + movimiento[0], coords[1] + movimiento[1]), solucion, d - 1, enemigos)
                    mapa[coords[0]][coords[1]] = 0
                else:
                    mapa[coords[0]][coords[1]] = -1
                    solucion = defender_ciudad(mapa, lim0, lim1, (coords[0] + movimiento[0], coords[1] + movimiento[1]), solucion, d - 1, enemigos - 1)
                    mapa[coords[0]][coords[1]] = 1
            recorrer += 1
    return solucion

def movimiento_factible(mapa: list, coords: tuple, lim0: int, lim1: int) -> bool:
    if 0 <= coords[0] <= lim0 and 0 <= coords[1] <= lim1 and mapa[coords[0]][coords[1]] != -1:
        return True
    else:
        return False
    
def es_solucion(enemigos: int,coords: tuple, mapa: list) -> bool:
    if enemigos == 1 and mapa[coords[0]][coords[1]] == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    n, m, e = map(int, input().strip().split())
    mapa = []
    for i in range(n):
        mapa.append(list(map(int, input().strip().split())))
    x, y, d = map(int, input().strip().split())
    sol = defender_ciudad(mapa, n - 1, m - 1, (x, y), False, d, e)
    if sol:
        print("ATACA")
    else:
        print("CORRE")