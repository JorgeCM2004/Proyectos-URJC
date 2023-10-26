from scipy.optimize import linprog

# Coeficientes de la función objetivo (que queremos minimizar)
obj = [-24, -18]  # Coeficiente de x1, Coeficiente de x2.

# Coeficientes del lado izquierdo de las inecuaciones
lhs_ineq = [[3, 4], [3, 3], [4, 2]]

# Lado derecho de las inecuaciones
rhs_ineq = [12, 10, 8]

# Coeficientes del lado izquierdo de las ecuaciones
lhs_eq = 'No hay ecuaciones.'

# Lado derecho de las ecuaciones
rhs_eq = 'No hay ecuaciones.'

# Límites para las variables (x, x2)
bnd = [(0, float('inf')),  # Límites para x1
       (0, float('inf'))]  # Límites para x2

# Resolviendo el problema de programación lineal
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd)

# Mostrando los resultados
print("Valor mínimo de la función objetivo:", opt.fun)
print("¿Se encontró una solución?", opt.success)
print("Valores de (x, y):", opt.x)