# 01_numpy_basico.py - Creación de arreglos con NumPy
import numpy as np
 
print("Versión de NumPy:", np.__version__)
 
# 1. Crear un arreglo a partir de una lista
notas = np.array([14, 16, 11, 18, 13])
print("Arreglo de notas:", notas)
print("Tipo de dato:", notas.dtype)
print("Dimensiones (shape):", notas.shape)
 
# 2. Arreglos especiales
ceros = np.zeros(4)
unos = np.ones((2, 3))
rango = np.arange(0, 10, 2)        # inicio, fin (excluido), paso
lineal = np.linspace(0, 1, 5)      # 5 valores entre 0 y 1
print("Ceros:", ceros)
print("Unos (2x3):\n", unos)
print("arange:", rango)
print("linspace:", lineal)
 
# 3. Arreglo de 2 dimensiones (matriz) y reshape
matriz = np.arange(1, 13).reshape(3, 4)
print("Matriz 3x4:\n", matriz)
print("Número de dimensiones:", matriz.ndim, "| Total de elementos:", matriz.size)
