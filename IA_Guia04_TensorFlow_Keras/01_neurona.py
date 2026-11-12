import numpy as np
 
# Entradas (como las dendritas): horas de estudio, asistencia (0 a 1), tareas entregadas
x = np.array([6.0, 0.9, 4.0])
 
# Pesos: importancia de cada entrada (la "fuerza" de cada sinapsis)
w = np.array([0.4, 2.0, 0.3])
b = -4.0                                     # sesgo (bias): umbral de activación
 
# 1. Suma ponderada (lo que hace el cuerpo de la neurona)
z = np.dot(x, w) + b
print("Suma ponderada z =", round(z, 3))
 
# 2. Función de activación sigmoide: convierte z en un valor entre 0 y 1
def sigmoide(z):
    return 1 / (1 + np.exp(-z))
 
salida = sigmoide(z)
print("Salida de la neurona (probabilidad de aprobar):", round(salida, 3))
print("Decisión:", "Aprueba" if salida >= 0.5 else "Desaprueba")
 
# 3. Probar con otro estudiante
x2 = np.array([1.0, 0.5, 1.0])
print("Estudiante 2 -> salida:", round(sigmoide(np.dot(x2, w) + b), 3))
