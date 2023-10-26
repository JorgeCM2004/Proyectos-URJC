#No reduce nada.
'''def verdadero_round(a: float):
    a = str(a)
    _, d = a.split('.')
    a = float(a)
    a = int(a)
    if int(d[0]) > 5:
        return a + 1
    elif int(d[0]) < 5:
        return a
    else:
        if len(d) == 1:
            return a + 1
        else:
            return a
def pow(x: float, a: int):
    if a == 1:
        return x
    else:
        x1 = pow(x, verdadero_round(a / 2))
        x2 = pow(x, a // 2)
        return x1 * x2
a = 10
b = 100
c = pow(a, b)
count = 0
for i in str(c):
    if i == '0':
        count += 1
print(c, count)'''
#Codigo bien hecho.
def pot(x, a):
    if a == 0:
        return 1
    else:
        if a % 2 == 0:
            aux = pot(x, a//2)
            result = aux * aux
        else:
            result = x * pot(x, a-1)
    return result

x = int(input("Numero: "))
a = int(input("Elevado a: "))
Z = pot(x, a)
print(Z)