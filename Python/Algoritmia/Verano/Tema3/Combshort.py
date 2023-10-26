def combshort(array):
    ordenada = False
    gap  = len(array) - 1
    while(not ordenada or gap != 1):
        ordenada = True
        for i in range(len(array) - gap):
            if array[i] > array[i + gap]:
                aux = array[i]
                array[i] = array[i + gap]
                array[i + gap] = aux
                ordenada = False
        if gap != 1:
            gap = int(gap // 1.3)
    return array

print(combshort([12, 3, -2, 1, 7, 8, -21]))