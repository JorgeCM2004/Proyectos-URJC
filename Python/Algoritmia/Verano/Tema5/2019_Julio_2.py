def vectorTransformado(l, n):
    for _ in range(n):
        min_index = 0
        for i in range(len(l)):
            if l[i] < l[min_index]:
                min_index = i
        l[min_index] *= -1
    return l

print(vectorTransformado([-2, -10, -20, 5, -1, 2], 3))