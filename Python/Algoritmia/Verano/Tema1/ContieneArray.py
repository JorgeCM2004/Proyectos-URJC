def contienearray(n, array):
    # return array.__contains__(n)
    bol  = False
    indice =  0
    while(not bol and indice < len(array)):
        if array[indice] == n:
            bol = True
        indice += 1
    return bol

print(contienearray(9, [1, 2, 3, 4]))