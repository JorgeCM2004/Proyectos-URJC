a = int(input())
b = int(input())
contador = 0
c = input()
lista = []
concat = ''
for i in c:
    if i == ' ':
        lista.append(int(concat))
        concat = ''
    else:
        concat += i
lista.append(int(concat))
max = 0
min = 0
for i in lista:
    if i >= b:
        contador += 1
    if i > lista[max]:
        max = lista.index(i)
    if i < lista[min]:
        min = lista.index(i)

print(min, max, contador)