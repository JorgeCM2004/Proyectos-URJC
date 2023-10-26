a = input()
a = a[:-3]
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in a:  
    if i != ' ':
        l[int(i)] += 1
out = ''
for i in range(len(l), ):
    if l[i] > 2:
        out += str(i) + ' '
out = out[:-1]
print(out)