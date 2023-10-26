def ordenaporburbuja(array):
    for i in range(len(array), 0, -1):
        for x in range(0, i - 1):
            if array[x] > array[x + 1]:
                aux = array[x + 1]
                array[x + 1] = array[x]
                array[x] = aux
    return array

print(ordenaporburbuja([2, 1, 4, 5, 3]))