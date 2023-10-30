def comparar_palabras(palabra1: str, palabra2: str) -> bool:
    for i in range(len(palabra1)):
        letra1 = ord(palabra1[i])
        letra2 = ord(palabra2[i])
        if letra1 > letra2:
            return True
        elif letra1 < letra2:
            return False

def encontrar_universo(array: list, i: int, f: int, buscar: str) -> int:
    k = (i + f) // 2
    if array[k] == buscar:
        return k
    else:
        if comparar_palabras(array[k], buscar):
            return encontrar_universo(array, i, k - 1, buscar)
        else:
            return encontrar_universo(array, k + 1, f, buscar)    
lista = list(map(str, input().strip().split()))
longitud = len(lista) - 1
lista.sort()
num = int(input())
for i in range(num):
    busca = input()
    index = encontrar_universo(lista, 0, longitud, busca)
    if index - 1 < 0 and index + 1 > longitud:
        print("VACIO VACIO")
    elif index - 1 < 0:
        print(f"VACIO {lista[index + 1]}")
    elif index + 1 > longitud:
        print(f"{lista[index - 1]} VACIO")
    else:
        print(f"{lista[index - 1]} {lista[index + 1]}")
