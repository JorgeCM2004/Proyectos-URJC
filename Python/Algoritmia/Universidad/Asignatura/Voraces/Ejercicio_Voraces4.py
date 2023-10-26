def ordenar_tareas(diccionario, out):
    for i in range(len(diccionario['b'])):
        index = diccionario['b'].index(max(diccionario['b']))  
        if out[diccionario['f'][index]] == '':
            out[diccionario['f'][index]] = index + 1
            diccionario['b'][index] = 0
    return out 

num_dias = int(input("Dame el numero de dias disponibles: "))
tareas = {'b': [], 'f': []}
plan = []
for i in range(num_dias):
    plan.append('')
for i in range(num_dias):
    tareas['b'].append(int(input(f"Dame el beneficio de la tarea {i + 1}: ")))
    tareas['f'].append(int(input(f"Dame la fecha límite de la tarea {i + 1}: ")))
for i in range(max(tareas['f'])):
    plan.append('')
plan = ordenar_tareas(tareas, plan)
while '' in plan:
    plan.remove('')
print(plan)