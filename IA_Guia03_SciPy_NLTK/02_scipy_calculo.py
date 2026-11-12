# 02_scipy_calculo.py - Optimización, integración, álgebra lineal e interpolación
import numpy as np
from scipy import optimize, integrate, linalg, interpolate
 
# 1. Optimización: encontrar el mínimo de f(x) = (x - 3)² + 2
def f(x):
    return (x - 3) ** 2 + 2
 
resultado = optimize.minimize_scalar(f)
print(f"Mínimo en x = {resultado.x:.4f}, f(x) = {resultado.fun:.4f}")
 
# 2. Ajuste de curvas: encontrar a y b en y = a·x + b
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1.1, 2.9, 5.2, 7.1, 8.8, 11.2])
def recta(x, a, b):
    return a * x + b
(a, b), _ = optimize.curve_fit(recta, x, y)
print(f"Recta ajustada: y = {a:.3f}x + {b:.3f}")
 
# 3. Integración numérica: área bajo x² entre 0 y 3
area, error = integrate.quad(lambda t: t ** 2, 0, 3)
print(f"Integral de x² de 0 a 3 = {area:.4f}")
 
# 4. Álgebra lineal: resolver el sistema
#    2x + 3y = 8
#    3x -  y = 1
A = np.array([[2, 3], [3, -1]])
b_vec = np.array([8, 1])
solucion = linalg.solve(A, b_vec)
print("Solución del sistema (x, y):", solucion)
print("Determinante de A:", round(linalg.det(A), 2))
 
# 5. Interpolación: estimar valores intermedios (spline cúbico)
horas = np.array([0, 2, 4, 6, 8])
temperatura = np.array([15, 18, 24, 22, 17])
interp = interpolate.CubicSpline(horas, temperatura)
print("Temperatura estimada a las 5 h:", round(float(interp(5)), 2))
