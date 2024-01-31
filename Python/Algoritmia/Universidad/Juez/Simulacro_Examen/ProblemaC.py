def esSolucion(coords: tuple, fin: tuple) -> list:
    return coords[0] == fin[0] and coords[1] == fin[1]

def esFactible(laberinto: list, coords: tuple, limites: tuple) -> bool:
    return 0 <= coords[0] < limites[0] and 0 <= coords[1] < limites[1] and laberinto[coords[0]][coords[1]] != 'w'

def resolver_laberinto(laberinto: list, coords: tuple, tesoros: int, tesorosRecogidos: int, fin: tuple, pasos: int, limites: tuple) -> int:
    if esSolucion(coords, fin):
        return [(tesorosRecogidos, pasos)]
    else:
        soluciones_parciales = []
        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in movimientos:
            newcoords = (coords[0] + i[0], coords[1] + i[1])
            if esFactible(laberinto, newcoords, limites):
                if laberinto[newcoords[0]][newcoords[1]] == 'x':
                    recordar = laberinto[coords[0]][coords[1]]
                    laberinto[coords[0]][coords[1]] = 'w'
                    sol = resolver_laberinto(laberinto, newcoords, tesoros, tesorosRecogidos + 1, fin, pasos + 1, limites)
                    laberinto[coords[0]][coords[1]] = recordar
                else:
                    recordar = laberinto[coords[0]][coords[1]]
                    laberinto[coords[0]][coords[1]] = 'w'
                    sol = resolver_laberinto(laberinto, newcoords, tesoros, tesorosRecogidos, fin, pasos + 1, limites)
                    laberinto[coords[0]][coords[1]] = recordar
                if sol:
                    soluciones_parciales += sol
        if soluciones_parciales:
            return soluciones_parciales

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    laberinto = []
    tesoros = 0
    for i in range(n):
        linea = list(map(str, input().strip().split()))
        for x in range(m):
            if linea[x] == 'x':
                tesoros += 1
            elif linea[x] == 's':
                start = (i, x)
            elif linea[x] == 'e':
                end = (i, x)
        laberinto.append(linea)
    for i in range(n):
        for x in range(m):
            if laberinto[i][x] == 'u' and i - 1 >= 0:
                laberinto[i][x] = 'w'
                if laberinto[i - 1][x] == 'x':
                    tesoros -= 1
                laberinto[i - 1][x] = 'w'
            elif laberinto[i][x] == 'd' and i + 1 < n:
                laberinto[i][x] = 'w'
                if laberinto[i + 1][x] == 'x':
                    tesoros -= 1
                laberinto[i + 1][x] = 'w'
            elif laberinto[i][x] == 'l' and x - 1 >= 0:
                laberinto[i][x] = 'w'
                if laberinto[i][x - 1] == 'x':
                    tesoros -= 1
                laberinto[i][x - 1] = 'w'
            elif laberinto[i][x] == 'r' and x + 1 < m:
                laberinto[i][x] = 'w'
                if laberinto[i][x + 1] == 'x':
                    tesoros -= 1
                laberinto[i][x + 1] = 'w'
    soluciones = resolver_laberinto(laberinto, start, tesoros, 0, end, 0, (n, m))
    soluciones.sort(reverse= True)
    max_tesoros = soluciones[0][0]
    distancia_min = soluciones[0][1]
    recorrer = 1
    while recorrer < len(soluciones) and soluciones[recorrer][0] == max_tesoros:
        if soluciones[recorrer][1] < distancia_min:
            distancia_min = soluciones[recorrer][1]
        recorrer += 1
    print(max_tesoros, distancia_min)
