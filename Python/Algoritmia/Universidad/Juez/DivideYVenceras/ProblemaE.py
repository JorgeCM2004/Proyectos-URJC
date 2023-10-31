def encontrar_generacion(array: list, buscando: int, iteraciones: int) -> int:
    if len(array[buscando]) == 0:
        return iteraciones
    else:
        out = []
        for x in array[buscando]:
            out.append(encontrar_generacion(lista, x, iteraciones + 1))
        return max(out)

num = int(input())
lista = []
for x in range(num):
    lista.append([])
for i in range(num):
    familia = list(map(int, input().strip().split()))
    padre = familia[0]
    for j in familia[1:]:
        lista[j].append(padre)
num_busca = int(input())
for i in range(num_busca):
    buscando = int(input())
    print(encontrar_generacion(lista, buscando, 1))
