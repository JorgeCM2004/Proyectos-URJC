def backtracking(l: list, n: int, pos: int) -> list:
    if pos == n and factible(l):
        return l
    recorrer = 0
    while recorrer < n and pos < n:
        l[pos] = recorrer
        if (factible(l)):
            resultado = backtracking(l, n, pos + 1)
            if resultado is not None and factible(resultado):
                return resultado
        l[pos] = None
        recorrer += 1
    return None

            
def factible(l: list) -> bool:
    laux = []
    recorrer = 0
    while recorrer < len(l) and l[recorrer] != None:
        laux.append(l[recorrer])
        recorrer += 1
    out = True
    recorrer = 0
    while out and recorrer < len(laux) - 1:
        if conflicto(len(laux) - 1, laux[len(laux) - 1], recorrer, laux[recorrer]):
            out = False
        recorrer += 1
    return out

def conflicto(xdama1: int, ydama1: int, xdama2: int, ydama2: int):
    return (xdama1 + ydama1) == (xdama2 + ydama2) or (xdama1 - ydama1) == (xdama2 - ydama2) or xdama1 == xdama2 or ydama1 == ydama2

num = int(input("Introduzca cuantas damas (n) se deberian colocar en el tablero (n * n) sin que se amenacen entre ellas: "))
lista = [None] * num
respuesta = backtracking(lista, num, 0)
blanco = True
if respuesta:
    for x in range(num):
        for y in range(num):
            if respuesta[x] == y:
                print('👑', end='')
            else:
                if blanco:
                    print('⬜', end='')
                else:
                    print('⬛', end='')
            blanco = not blanco
        if num % 2 == 0:
            blanco = not blanco
        print()
else:
    print(f"No existe solucion posible para el problema de las {num} damas.")