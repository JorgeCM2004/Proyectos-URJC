def matriztraspuesta(matriz):
    mtras = []
    for i in range(len(matriz[0])):
        mtras.append([])

    for i in range(len(matriz)):
        for x in range(len(matriz[i])):
            mtras[x].append(matriz[i][x])
    return mtras

print(matriztraspuesta([[1, 2, 3], [4, 5, 6]]))