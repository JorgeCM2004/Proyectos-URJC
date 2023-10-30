import sys
def buscar_penny(array, i, f, intentos, posicion) -> tuple:
    k = (i + f) // 2
    if array[k] == posicion:
        return intentos, k
    else:
        if array[k] > posicion:
            return buscar_penny(array, i, k - 1, intentos + 1, posicion)
        else:
            return buscar_penny(array, k + 1, f, intentos + 1, posicion)
a, b, c = map(int, input().strip().split())
lista = list(map(int, input().strip().split()))
intentos, ubicacion = buscar_penny(lista, 0, a - 1, 1, c)
if intentos > b:
    sys.stdout.buffer.write("¿Donde esta Penny?".encode('utf-8'))
else:
    print(f"Penny esta en la habitacion {ubicacion}, se han requerido {intentos} saltos")