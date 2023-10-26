from scipy.optimize import linprog

# Coeficientes de la función objetivo (que queremos minimizar)
obj = [-1, -2]  # Coeficiente de x, Coeficiente de y

# Coeficientes del lado izquierdo de las inecuaciones
lhs_ineq = [[2, 1], [-3, 5], [1, -2]]

# Lado derecho de las inecuaciones
rhs_ineq = [20, 10, 2]

# Coeficientes del lado izquierdo de las ecuaciones
lhs_eq = [[-1, 5]]

# Lado derecho de las ecuaciones
rhs_eq = [15]

# Límites para las variables (x, y)
bnd = [(0, float('inf')),  # Límites para x
       (0, float('inf'))]  # Límites para y

# Resolviendo el problema de programación lineal
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd)

# Mostrando los resultados
print("Valor mínimo de la función objetivo:", opt.fun)
print("¿Se encontró una solución?", opt.success)
print("Valores de (x, y):", opt.x)