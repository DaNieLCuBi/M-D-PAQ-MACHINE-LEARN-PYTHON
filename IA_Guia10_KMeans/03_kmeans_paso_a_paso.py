# 03_kmeans_paso_a_paso.py - Cómo "piensa" K-Means, programado con NumPy 
import numpy as np 
  
puntos = np.array([[1, 2], [1.5, 1.8], [1, 0.6], [5, 8], 
                   [8, 8], [9, 11], [8, 2], [9, 3]]) 
k = 2 
centroides = puntos[[0, 3]].astype(float)       # 1) INICIALIZACIÓN: k centroides 
print("Centroides iniciales:\n", centroides) 
  
for it in range(1, 11): 
    # 2) ASIGNACIÓN: cada punto va al centroide más cercano (distancia euclidiana) 
    distancias = np.linalg.norm(puntos[:, None] - centroides[None, :], axis=2) 
    grupo = distancias.argmin(axis=1) 
    # 3) ACTUALIZACIÓN: cada centroide pasa al promedio de sus puntos 
    nuevos = np.array([puntos[grupo == j].mean(axis=0) for j in range(k)]) 
    print(f"Iteración {it}: grupos = {grupo} | centroides = 
{nuevos.round(2).tolist()}") 
    # 4) CONVERGENCIA: si los centroides ya no se mueven, terminamos 
    if np.allclose(nuevos, centroides): 
        print("Los centroides no cambiaron: el algoritmo CONVERGIÓ.") 
        break 
    centroides = nuevos