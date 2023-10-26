def intercambiar(Array, ini, i_decrez):
    aux = Array[ini]
    Array[ini] = Array[i_decrez]
    Array[i_decrez] = aux
    return Array

def pivote(Array, ini, fin):
    ValPivote = Array[ini]
    i_crez = ini + 1
    i_decrez = fin
    hecho = 0
    while not hecho:
        while i_crez <= i_decrez and Array[i_crez] <= ValPivote:
            i_crez += 1
        while Array[i_decrez] >= ValPivote and i_decrez >= i_crez:
            i_decrez -= 1
        if i_decrez < i_crez:
            hecho = True
        else:
            Array = intercambiar(Array, i_crez, i_decrez)
    Array = intercambiar(Array, ini, i_decrez)
    return Array, i_decrez

def quicksort(array, ini, fin):
    if ini < fin :
        [array, b] = pivote(array, ini, fin)
        array = quicksort(array, ini, b - 1)
        array = quicksort(array, b + 1, fin)
    return array


dato = [2, 41, 12, 53, 3, 6, -1, 5, 6, 11, 8, 4]
Orden = quicksort(dato, 0, len(dato)-1)
print(Orden)