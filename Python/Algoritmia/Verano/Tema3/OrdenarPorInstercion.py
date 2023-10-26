def ordenaporinsercion(array):
    for i in range(len(array)):
        num = array[i]
        while(i > 0 and array[i - 1] > num):
            array[i] = array[i-1]
            i -= 1
        array[i] = num
    return array

print(ordenaporinsercion([2, 1, 4, 5, 3]))