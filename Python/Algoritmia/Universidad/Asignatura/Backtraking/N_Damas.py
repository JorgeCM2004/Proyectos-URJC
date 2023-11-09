def backtraking(l: list, n: int, pos: int) -> list:
    bol = None not in l
    if bol:
        return l
    else:
        recorrer = 0
        while recorrer < n and not bol:
            l[pos] = recorrer
            if factible(l):
                return backtraking(l, n, pos + 1)
            recorrer += 1
            
def factible(l: list) -> bool:
    laux = []
    recorrer = 0
    while recorrer < len(l) - 1 and l[recorrer] != None:
        laux.append(l[recorrer])
        recorrer += 1
    out = True
    recorrer = 0
    while out and recorrer < len(laux) - 1:
        if conflicto(len(laux) - 1, laux[len(laux) - 1], recorrer, laux[recorrer]):
            out = False
        recorrer += 1
    return out

def conflicto(xdama1: int, ydama1: int, xdama2: int, ydama2: int):
    return (xdama1 + ydama1) == (xdama2 + ydama2) or (xdama1 - ydama1) == (xdama2 - ydama2) or xdama1 == xdama2 or ydama1 == ydama2

num = int(input())
lista = [None] * num
repuesta = backtraking(lista, num, 0)
print(repuesta)