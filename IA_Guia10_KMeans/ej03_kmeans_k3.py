# ej03_kmeans_k3.py - K-Means paso a paso con k = 3 
import numpy as np 
  
puntos = np.array([[1, 2], [1.5, 1.8], [1, 0.6], [5, 8], 
                   [8, 8], [9, 11], [8, 2], [9, 3]]) 
k = 3                                            # CAMBIO: 3 grupos 
centroides = puntos[[0, 3, 6]].astype(float)     # CAMBIO: tercer centroide = punto (8, 2) 
print("Centroides iniciales:\n", centroides) 
  
for it in range(1, 11): 
    distancias = np.linalg.norm(puntos[:, None] - centroides[None, :], axis=2) 
    grupo = distancias.argmin(axis=1) 
    nuevos = np.array([puntos[grupo == j].mean(axis=0) for j in range(k)]) 
    print(f"Iteración {it}: grupos = {grupo} │ centroides = {nuevos.round(2).tolist()}") 
    if np.allclose(nuevos, centroides): 
        print(f"Los centroides no cambiaron: el algoritmo CONVERGIÓ en la iteración {it}.") 
        break 
    centroides = nuevos 
  
# EXTRA: inercia = suma de distancias² de cada punto a su centroide 
inercia = ((puntos - centroides[grupo]) ** 2).sum() 
print(f"Inercia final: {inercia:.2f}") 