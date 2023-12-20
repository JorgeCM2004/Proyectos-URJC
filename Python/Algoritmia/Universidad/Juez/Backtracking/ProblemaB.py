def encontrar_piezas(edificio: list, lim0: int, lim1: int, coords: tuple, recogidos: int, p: int, pasos: int) -> int:
    if es_solucion(edificio, coords, recogidos, p):
        return pasos
    else:
        sol = []
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for movimiento in movimientos:
            if movimiento_factible(edificio, (coords[0] + movimiento[0], coords[1] + movimiento[1]), recogidos, lim0, lim1):
                recordar = edificio[coords[0]][coords[1]]
                edificio[coords[0]][coords[1]] = p + 1
                if edificio[coords[0] + movimiento[0]][coords[1] + movimiento[1]] == recogidos + 1:
                    recursividad = encontrar_piezas(edificio, lim0, lim1, (coords[0] + movimiento[0], coords[1] + movimiento[1]), recogidos + 1, p, pasos + 1)
                    if recursividad != None:
                        sol.append(recursividad)
                else:
                    recursividad = encontrar_piezas(edificio, lim0, lim1, (coords[0] + movimiento[0], coords[1] + movimiento[1]), recogidos, p, pasos + 1)
                    if recursividad != None:
                        sol.append(recursividad)
                edificio[coords[0]][coords[1]] = recordar
        if len(sol) > 0:
            return min(sol)

def movimiento_factible(edificio: list, coords: tuple, recogidos: int, lim0: int, lim1: int) -> bool:
    if 0 <= coords[0] <= lim0 and 0 <= coords[1] <= lim1 and edificio[coords[0]][coords[1]] <= recogidos + 1:
        return True
    else:
        return False
    
def es_solucion(edificio: list, coords: tuple, recogidos: int, p: int) -> bool:
    if recogidos == p:
        return True
    else:
        return False

if __name__ == "__main__":
    n, m, p = map(int, input().strip().split())
    edificio = []
    for i in range(n):
        edificio.append(list(map(int, input().strip().split())))
    print(encontrar_piezas(edificio, n - 1, m - 1, (0, 0), 0, p, 1))
