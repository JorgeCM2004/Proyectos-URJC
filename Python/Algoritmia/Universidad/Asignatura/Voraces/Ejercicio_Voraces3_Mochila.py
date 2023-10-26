def seleccionar_objetos(objetos, peso_max, mochila):
    while len(objetos['v/w']) > 0 and peso_max > 0:
        index = objetos['v/w'].index(max(objetos['v/w']))  
        if objetos['w'][index] <= peso_max:
            mochila[index] = 1
            peso_max -= objetos['w'][index]
            objetos['v/w'][index] = 0
        else:
            mochila[index] =  peso_max / objetos['w'][index]
            peso_max = 0
    return mochila

peso_mochila = int(input("Dame la capacidad máxima de la mochila: "))
objetos = {'w': [], 'v': [], 'v/w': []}
num_objetos = int(input("Dame el numero de objetos que tienes: "))
mochila = []
for i in range(num_objetos):
    objetos['w'].append(int(input(f"Dame el peso del objeto {i + 1}: ")))
    objetos['v'].append(int(input(f"Dame el valor del objeto {i + 1}: ")))
    objetos['v/w'].append(objetos['v'][i]/objetos['w'][i])
    mochila.append(0)
print(seleccionar_objetos(objetos, peso_mochila, mochila))