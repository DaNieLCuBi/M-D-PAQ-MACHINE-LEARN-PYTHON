# 02_numpy_operaciones.py - Operaciones vectorizadas y estadísticas
import numpy as np
 
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
 
# 1. Operaciones elemento a elemento (sin bucles for)
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("Potencia:", b ** 2)
 
# 2. Broadcasting: operar un arreglo con un escalar
print("a + 5 =", a + 5)
 
# 3. Estadísticas básicas
notas = np.array([14, 16, 11, 18, 13, 9, 15])
print("Promedio:", notas.mean().round(2))
print("Máximo:", notas.max(), "| Mínimo:", notas.min())
print("Desviación estándar:", notas.std().round(2))
print("Mediana:", np.median(notas))
 
# 4. Indexación, slicing y máscaras booleanas
print("Primera nota:", notas[0], "| Última nota:", notas[-1])
print("Notas de la 2 a la 4:", notas[1:4])
aprobados = notas[notas >= 13]
print("Notas aprobatorias (>=13):", aprobados)
 
# 5. Operaciones con matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Producto matricial A @ B:\n", A @ B)
print("Transpuesta de A:\n", A.T)
print("Suma por columnas de A:", A.sum(axis=0))
print("Suma por filas de A:", A.sum(axis=1))
 
# 6. Números aleatorios reproducibles
rng = np.random.default_rng(seed=42)
aleatorios = rng.integers(0, 21, size=5)
print("5 notas aleatorias:", aleatorios)
