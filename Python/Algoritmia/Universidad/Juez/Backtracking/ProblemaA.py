def resolver_laberinto(laberinto: list, num: int, coords: tuple, solucion: bool, num_ceros: int) -> bool:
    if es_solucion(coords, num - 1, num_ceros):
        return True
    else:
        recorrer = 0
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while not solucion and recorrer < 4:
            movimiento = movimientos[recorrer]
            if movimiento_factible(laberinto, (coords[0] + movimiento[0], coords[1] + movimiento[1]), num - 1):
                laberinto[coords[0]][coords[1]] = -1
                solucion = resolver_laberinto(laberinto, num, (coords[0] + movimiento[0], coords[1] + movimiento[1]), solucion, num_ceros + 1)
                laberinto[coords[0]][coords[1]] = 0
            recorrer += 1
    return solucion

def movimiento_factible(laberinto: list, coords: tuple, long: int) -> bool:
    if 0 <= coords[0] <= long and 0 <= coords[1] <= long and laberinto[coords[0]][coords[1]] == 0:
        return True
    else:
        return False
    
def es_solucion(coords: tuple, long: int, num_ceros: int) -> bool:
    if coords == (long, long) and num_ceros == ceros - 1:
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input())
    laberinto = []
    ceros = 0
    for i in range(num):
        fila = list(map(int, input().strip().split()))
        ceros += fila.count(0)
        laberinto.append(fila)
    sol = resolver_laberinto(laberinto, num, (0, 0), False, 0)
    if sol:
        print("SI")
    else:
        print("NO")