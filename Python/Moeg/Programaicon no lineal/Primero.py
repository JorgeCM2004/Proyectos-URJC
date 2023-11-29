from scipy.optimize import minimize, Bounds

def quadratic_cost(x):
    return 0.1 * x[0] ** 2 + 2 * x[0] + 500

bounds_quad = Bounds([50], [250])
result = minimize(quadratic_cost, [100], bounds=bounds_quad, method='trust-constr')

print(result.fun)
print(result.x)