# 04_kmeans_clientes.py - Segmentación de clientes con K-Means (scikit-learn) 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.datasets import make_blobs 
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
  
# 1. PREPARACIÓN DE DATOS (dataset simulado de un centro comercial) 
X, _ = make_blobs(n_samples=200, centers=[[25, 20], [30, 80], [70, 50], [95, 20], [95, 
85]], 
                  cluster_std=[6, 6, 7, 6, 6], random_state=3) 
df = pd.DataFrame({"ingreso_mil": X[:, 0].round(1), "puntaje_gasto": X[:, 1].clip(1, 
100).round(0)}) 
df.to_csv("clientes.csv", index=False) 
print(df.describe().round(1)) 
  
escalador = StandardScaler()                 # pone ambas columnas en la misma escala 
X_esc = escalador.fit_transform(df) 
  
# 2. ENTRENAMIENTO 
km = KMeans(n_clusters=5, init="k-means++", n_init=10, random_state=42) 
df["grupo"] = km.fit_predict(X_esc) 
  
# 3. RESULTADOS 
centros = pd.DataFrame(escalador.inverse_transform(km.cluster_centers_), 
                       columns=["ingreso_mil", "puntaje_gasto"]).round(1) 
centros["clientes"] = df["grupo"].value_counts().sort_index().values 
print("\nCentroides de cada grupo (en escala original):") 
print(centros) 
print(f"\nInercia (suma de distancias²): {km.inertia_:.2f}") 
  
nuevo = pd.DataFrame({"ingreso_mil": [90], "puntaje_gasto": [88]}) 
print("Cliente nuevo (90 mil, gasto 88) -> grupo", 
km.predict(escalador.transform(nuevo))[0]) 
  
plt.scatter(df["ingreso_mil"], df["puntaje_gasto"], c=df["grupo"], cmap="tab10", s=30) 
plt.scatter(centros["ingreso_mil"], centros["puntaje_gasto"], c="black", marker="X", 
s=200, label="Centroides") 
plt.title("Segmentación de clientes con K-Means (k = 5)") 
plt.xlabel("Ingreso anual (miles de S/)"); plt.ylabel("Puntaje de gasto (1-100)") 
plt.legend(); plt.grid(alpha=0.3) 
plt.savefig("g10_clientes.png", dpi=110, bbox_inches="tight") 
plt.show()