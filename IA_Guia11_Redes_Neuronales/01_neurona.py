# 01_neurona.py - Una neurona artificial programada con NumPy 
import numpy as np 
  
# Entradas: características de un estudiante (valores entre 0 y 1) 
x = np.array([0.8, 0.3, 0.5])        # x1 = asistencia, x2 = horas de juego, x3 = 
tareas entregadas 
# Pesos: importancia de cada entrada (los "aprende" la red) 
w = np.array([0.6, -0.4, 0.9]) 
b = -0.2                              # sesgo (bias) 
  
# 1. Suma ponderada: z = x1·w1 + x2·w2 + x3·w3 + b 
z = np.dot(x, w) + b 
print("Entradas x :", x) 
print("Pesos   w :", w) 
print("Sesgo   b :", b) 
print(f"Suma ponderada z = {z:.3f}") 
  
# 2. Función de activación 
sigmoide = 1 / (1 + np.exp(-z)) 
relu = max(0, z) 
print(f"Salida con sigmoide : {sigmoide:.4f}") 
print(f"Salida con ReLU     : {relu:.4f}") 
  
# 3. Decisión final 
print("Predicción:", "APRUEBA" if sigmoide >= 0.5 else "DESAPRUEBA") 