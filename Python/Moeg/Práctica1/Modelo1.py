from scipy.optimize import linprog

# Coeficientes de la función objetivo (que queremos minimizar)
obj = [3, -5, 1]  # Coeficiente de x1, Coeficiente de x2, Coeficiente de x3.

# Coeficientes del lado izquierdo de las inecuaciones
lhs_ineq = 'No hay inecuaciones.'

# Lado derecho de las inecuaciones
rhs_ineq = 'No hay inecuaciones.'

# Coeficientes del lado izquierdo de las ecuaciones
lhs_eq = [[1, 0, -1], [3, 2, -7]]

# Lado derecho de las ecuaciones
rhs_eq = [1, 5]

# Límites para las variables (x, x2, x3)
bnd = [(0, float('inf')),  # Límites para x1
       (0, float('inf')),  # Límites para x2
       (0, float('inf'))]  # Límites para x3

# Resolviendo el problema de programación lineal
opt = linprog(c=obj, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd)

# Mostrando los resultados
print("Valor mínimo de la función objetivo:", opt.fun)
print("¿Se encontró una solución?", opt.success)
print("Valores de (x, y):", opt.x)