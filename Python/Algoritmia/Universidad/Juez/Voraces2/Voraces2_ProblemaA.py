n, m = map(int, input().strip().split())
almendritas = {'v': [], 'p': [], 'v/p': []}
for i in range(n):
    v, p = map(int, input().strip().split())
    almendritas['v'].append(v)
    almendritas['p'].append(p)
    almendritas['v/p'].append(v/p)
for i in range(m):
    mv, mp = map(int, input().strip().split())
    almendras = []
    for i in almendritas['v/p']:
        almendras.append(i)
    while mv > 0:
        index = almendras.index(max(almendras))
        if mv >= almendritas['v'][index]:
            mv -= almendritas['v'][index]
            mp -= almendritas['p'][index]
            almendras[index] = 0
        else:
            coef = mv / almendritas['v'][index] 
            mv = 0
            mp -= almendritas['p'][index] * coef
    if mp < 0:
        print("TOS")
    else:
        print("PUEDE")
    