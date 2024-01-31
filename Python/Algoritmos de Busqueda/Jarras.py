def rellenar(estado: tuple, finales: list, maximos: tuple, memory: list, sol: bool) -> bool:
    if esSolucion(estado, finales):
        return True
    else:
        memory.append(estado)
        combinando = 0
        while combinando < len(maximos) and not sol:
            nuevo_estado = grifo(estado, maximos, combinando)
            if estado_factible(nuevo_estado, memory):
                sol = rellenar(nuevo_estado, finales, maximos, memory, sol)
            combinando += 1
        combinando = 0
        while combinando < len(maximos) and not sol:
            nuevo_estado = vaciar(estado, combinando)
            if estado_factible(nuevo_estado, memory):
                sol = rellenar(nuevo_estado, finales, maximos, memory, sol)
            combinando += 1
        combinando = 0
        while combinando < len(maximos) and not sol:
            combinando1 = 0
            while combinando1 < len(maximos) and not sol:
                if combinando != combinando1:
                    nuevo_estado = moverAtoB(estado, maximos, combinando, combinando1)
                    if estado_factible(nuevo_estado, memory):
                        sol = rellenar(nuevo_estado, finales, maximos, memory, sol)
                combinando1 += 1
            combinando += 1
        return sol

def estado_factible(estado: tuple, memo: list) -> bool:
    for i in memo:
        recorrer = 0
        iguales = True
        while iguales and recorrer < len(i):
            if i[recorrer] != estado[recorrer]:
                iguales = False
            recorrer += 1
        if iguales:
            return not iguales
    return not iguales

def esSolucion(estado: tuple, f: list) -> bool:
    for i in f:
        seguir = True
        for x in range(len(i)):
            if i[x] != estado[x]:
                seguir = False
        if seguir:
            return True
    return False

def moverAtoB(estado: tuple, m: tuple, A: int, B: int):
    espacioB = m[B] - estado[B]
    estado = list(estado)
    if espacioB < estado[A]:
        estado[A] = estado[A] - espacioB
        estado[B] = m[B]
    else:
        estado[B] = estado[B] + estado[A]
        estado[A] = 0
    return tuple(estado)

def vaciar(estado: tuple, indice: int) -> tuple:
    if indice == 0:
        return (0, estado[1 - indice])
    return (estado[1 - indice], 0)

def grifo(estado: tuple, m: tuple, indice: int) -> tuple:
    if indice == 0:
        return (m[indice], estado[1 - indice])
    return (estado[1 - indice], m[indice])

if __name__ == "__main__":
    maximos = (4, 3)
    inicio = (0, 0)
    finales = []
    for i in range(maximos[1] + 1):
        finales.append((2, i))
    print(rellenar(inicio, finales, maximos, [], False))