def cambiar_numero_de_serie(listado: list, antiguoID: int, nuevoID: int) -> list:
    for i in range(len(listado)):
        if listado[i] == antiguoID:
            listado[i] = nuevoID
    return listado

def robotines(numero_de_robots: int, wifi: list) -> tuple:
    numero_de_serie = list(range(numero_de_robots))
    megas_que_consume = 0
    red_robots = [[0, []] for _ in range(numero_de_robots)]
    i = 0
    wifi.sort()
    while len(wifi) > i:
        w, r1, r2 = wifi[i]
        if numero_de_serie[r1] != numero_de_serie[r2]:          
            megas_que_consume += w
            red_robots[r1][0] += w
            red_robots[r2][0] += w
            red_robots[r1][1].append(r2)
            red_robots[r2][1].append(r1)
            numero_de_serie = cambiar_numero_de_serie(numero_de_serie, numero_de_serie[r1], numero_de_serie[r2])
        i += 1
    return (megas_que_consume, red_robots)

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for i in range(m):
        r1, r2, w = map(int, input().strip().split())
        edges.append((w, r1, r2))
    sol, conexiones = robotines(n, edges)
    print(sol)
    p = int(input())
    for _ in range(p):
        r = int(input())
        conexiones[r][1].sort()
        print(f"{conexiones[r][0]}:", end=' ')
        for i in range(len(conexiones[r][1])):
            print(conexiones[r][1][i], end=' ')
        print()
