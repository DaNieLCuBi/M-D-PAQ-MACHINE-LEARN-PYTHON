# ej01_perceptron_and.py - Perceptrón que aprende la compuerta AND 
import numpy as np 
  
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])   # entradas 
y = np.array([0, 0, 0, 1])                       # salida AND 
  
w = np.zeros(2)          # pesos iniciales 
b = 0.0                  # sesgo inicial 
tasa = 0.1               # tasa de aprendizaje 
  
def escalon(z): 
    return 1 if z >= 0 else 0 
  
for epoca in range(1, 21): 
    errores = 0 
    for xi, objetivo in zip(X, y): 
        pred = escalon(np.dot(xi, w) + b) 
        error = objetivo - pred 
        if error != 0:                           # regla del perceptrón 
            w += tasa * error * xi 
            b += tasa * error 
            errores += 1 
    print(f"Época {epoca}: errores = {errores} | w = {w.round(2)} | b = {b:.2f}") 
    if errores == 0: 
        print("¡Aprendió la compuerta AND!") 
        break 
  
print("\nx1 x2 | AND | perceptrón") 
for xi, objetivo in zip(X, y): 
    print(f" {xi[0]}  {xi[1]} |  {objetivo}  |     {escalon(np.dot(xi, w) + b)}") 