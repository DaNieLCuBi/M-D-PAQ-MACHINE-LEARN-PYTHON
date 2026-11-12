# ej04_notas.py - K-Means con un dataset propio: notas de Python y Matemática 
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score 
  
# 1. CREAR DATOS FICTICIOS (60 estudiantes, notas de 0 a 20) 
rng = np.random.default_rng(7) 
perfiles = [(17, 16, 15), (15, 8, 15), (8, 15, 15), (9, 8, 15)]  # (media Python, media Mate, n) 
filas = [np.column_stack([rng.normal(mp, 1.5, n), rng.normal(mm, 1.5, n)]) 
         for mp, mm, n in perfiles] 
X = np.vstack(filas).clip(0, 20).round(1) 
df = pd.DataFrame(X, columns=["nota_python", "nota_matematica"]) 
df.insert(0, "estudiante", [f"E{i:02d}" for i in range(1, len(df) + 1)]) 
df.to_csv("notas.csv", index=False) 
print("Filas:", len(df)) 
  
# 2. ESCALAR Y ELEGIR k CON LA SILUETA 
datos = df[["nota_python", "nota_matematica"]] 
esc = StandardScaler() 
Xe = esc.fit_transform(datos) 
print(" k  silueta") 
for k in range(2, 7): 
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(Xe) 
    print(f"{k:>2}  {silhouette_score(Xe, km.labels_):.3f}") 
  
# 3. ENTRENAR CON EL MEJOR k E INTERPRETAR 
km = KMeans(n_clusters=4, n_init=10, random_state=42).fit(Xe) 
df["grupo"] = km.labels_ 
c = pd.DataFrame(esc.inverse_transform(km.cluster_centers_), columns=datos.columns).round(1) 
c["estudiantes"] = df["grupo"].value_counts().sort_index().values 
print(c)