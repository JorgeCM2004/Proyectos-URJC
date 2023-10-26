def cambio(n, lista):
    lista.reverse()
    out = []
    for i in lista:
        out.append(n // i)
        n %= i
    if n == 0:
        return out
    else:
        return 'null'

d = int(input('Dame el dinero que necesitas cambiar: '))
l = input('Dame las monedas que dispones: ')
monedas = []
acum = ''
for i in l:
    if i == ' ':
        monedas.append(int(acum))
        acum = ''
    else:
        acum += i
monedas.append(int(acum))
monedas.sort()
total = cambio(d, monedas)
if total == 'null':
    print('No se puede cambiar esa cantidad con las monedas disponibles')
else:
    print("Necesitarás:")
    for i in range(len(monedas)):
        if total[i] != 0:
            print(total[i], "monedas de", monedas[i], "céntimos.")