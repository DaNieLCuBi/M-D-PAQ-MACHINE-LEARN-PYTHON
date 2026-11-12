# 03_red_numpy.py - Estructura de una red 3-4-2: neuronas, capas y conexiones 
import numpy as np 
  
np.random.seed(1) 
# Capa de entrada: 3 neuronas | Capa oculta: 4 neuronas | Capa de salida: 2 neuronas 
W1 = np.random.randn(3, 4).round(2)   # conexiones entrada -> oculta (3 x 4 = 12 pesos) 
b1 = np.zeros(4)                      # 4 sesgos 
W2 = np.random.randn(4, 2).round(2)   # conexiones oculta -> salida (4 x 2 = 8 pesos) 
b2 = np.zeros(2)                      # 2 sesgos 
  
def relu(z): return np.maximum(0, z) 
def softmax(z): 
    e = np.exp(z - z.max()) 
    return e / e.sum() 
  
x = np.array([0.5, 0.1, 0.9])         # un ejemplo de entrada 
h = relu(x @ W1 + b1)                 # propagación hacia adelante: capa oculta 
y = softmax(h @ W2 + b2)              # capa de salida 
  
print("Pesos W1 (entrada -> oculta):\n", W1) 
print("Salida de la capa oculta h:", h.round(3)) 
print("Pesos W2 (oculta -> salida):\n", W2) 
print("Probabilidades de salida y:", y.round(3)) 
print("Clase predicha:", y.argmax()) 
parametros = W1.size + b1.size + W2.size + b2.size 
print(f"Total de parámetros: {W1.size} + {b1.size} + {W2.size} + {b2.size} = 
{parametros}")