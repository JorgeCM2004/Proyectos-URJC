def ordenaporseleccion(array):
    for i in range(len(array)):
        min = array[i]
        pos = i 
        for x in range(i, len(array)):
            if array[x] < min:
                pos = x
                min = array[x]
        if pos != i:
            array[pos] = array[i]
            array[i] = min
    return array

print(ordenaporseleccion([2, 1, 4, 5, 3]))
