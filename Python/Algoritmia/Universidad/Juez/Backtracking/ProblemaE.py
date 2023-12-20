def escapa_con_cabeza(escenario: list, lim0: int, lim1: int, coords: tuple, recompensas: int, pasos: int) -> int:
    if es_solucion(escenario, coords, recompensas):
        return pasos
    else:
        sol = []
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for movimiento in movimientos:
            if movimiento_factible(escenario, (coords[0] + movimiento[0], coords[1] + movimiento[1]), lim0, lim1):
                recordar = escenario[coords[0]][coords[1]]
                escenario[coords[0]][coords[1]] = 'w'
                if escenario[coords[0] + movimiento[0]][coords[1] + movimiento[1]] == 'r':
                    recursividad = escapa_con_cabeza(escenario, lim0, lim1, (coords[0] + movimiento[0], coords[1] + movimiento[1]), recompensas + 1, pasos + 1)
                    if recursividad != None:
                        sol.append(recursividad)
                else:
                    recursividad = escapa_con_cabeza(escenario, lim0, lim1, (coords[0] + movimiento[0], coords[1] + movimiento[1]), recompensas, pasos + 1)
                    if recursividad != None:
                        sol.append(recursividad)
                escenario[coords[0]][coords[1]] = recordar
        if len(sol) > 0:
            return min(sol)

def movimiento_factible(escenario: list, coords: tuple, lim0: int, lim1: int) -> bool:
    if 0 <= coords[0] <= lim0 and 0 <= coords[1] <= lim1 and escenario[coords[0]][coords[1]] != 'w':
        return True
    else:
        return False
    
def es_solucion(escenario: list, coords: tuple, recompensas_faltantes: int) -> bool:
    if escenario[coords[0]][coords[1]] == 'r':
        recompensas_faltantes -= 1
    if recompensas_faltantes == 0 and coords == fin:
        return True
    else:
        return False

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    recompensas = 0
    inicio = 0
    fin = 0
    reemplazar = []
    escenario = []
    for i in range(n):
        fila = list(map(str, input().strip().split()))
        escenario.append(fila)
        recompensas += fila.count('r')
        if inicio == 0 and 's' in fila:
            inicio = (i, fila.index('s'))
        if fin == 0 and 'e' in fila:
            fin = (i, fila.index('e'))
        for x in range(m):
            if fila[x] == 't':
                reemplazar.append((i, x))
    moves360 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for i in reemplazar:
        for move in moves360:
            if escenario[i[0] + move[0]][i[1] + move[1]] == 'r':
                recompensas -= 1
            escenario[i[0] + move[0]][i[1] + move[1]] = 'w'
        
    print(escapa_con_cabeza(escenario, n - 1, m - 1, inicio, recompensas, 1))
