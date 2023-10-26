def ordenar(diccionario):
    out = []
    personas = diccionario['id']
    tiempos = diccionario['t']
    while len(tiempos) > 0:
        index = tiempos.index(min(tiempos))
        out.append(personas[index])
        personas.pop(index)
        tiempos.pop(index)
    return out

clientes = {'id': ['a', 'b', 'c', 'd'], 't': [3, 1, 5, 2]}
print(ordenar(clientes))