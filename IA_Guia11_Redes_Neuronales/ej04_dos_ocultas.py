# ej04_dos_ocultas.py - Red 3-4-3-2: se agrega una segunda capa oculta con tanh 
import numpy as np 
  
np.random.seed(1) 
W1 = np.random.randn(3, 4).round(2); b1 = np.zeros(4)   # entrada  -> oculta 1 
W2 = np.random.randn(4, 3).round(2); b2 = np.zeros(3)   # oculta 1 -> oculta 2 (NUEVA) 
W3 = np.random.randn(3, 2).round(2); b3 = np.zeros(2)   # oculta 2 -> salida 
  
def relu(z): return np.maximum(0, z) 
def softmax(z): 
    e = np.exp(z - z.max()) 
    return e / e.sum() 
  
x = np.array([0.5, 0.1, 0.9]) 
h1 = relu(x @ W1 + b1) 
h2 = np.tanh(h1 @ W2 + b2)          # segunda capa oculta con tanh 
y = softmax(h2 @ W3 + b3) 
  
print("Oculta 1 (ReLU):", h1.round(3)) 
print("Oculta 2 (tanh):", h2.round(3)) 
print("Probabilidades de salida:", y.round(3)) 
print("Clase predicha:", y.argmax()) 
p = [W1.size + b1.size, W2.size + b2.size, W3.size + b3.size] 
print(f"Parámetros por capa: {p} -> total = {sum(p)}") 