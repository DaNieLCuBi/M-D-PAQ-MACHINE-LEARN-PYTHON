# ej01_sin_escalar.py - Comparar K-Means con y sin StandardScaler 
import pandas as pd 
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
  
df = pd.read_csv("clientes.csv") 
print("Desviación estándar de cada columna:") 
print(df.std().round(1)) 
  
# A) CON escalado (como en la Práctica 04) 
esc = StandardScaler() 
km_con = KMeans(n_clusters=5, n_init=10, random_state=42).fit(esc.fit_transform(df)) 
c_con = pd.DataFrame(esc.inverse_transform(km_con.cluster_centers_), columns=df.columns).round(1) 
print("\nCentroides CON StandardScaler:") 
print(c_con.sort_values("ingreso_mil").to_string(index=False)) 
  
# B) SIN escalado: K-Means trabaja directamente con los valores originales 
km_sin = KMeans(n_clusters=5, n_init=10, random_state=42).fit(df) 
c_sin = pd.DataFrame(km_sin.cluster_centers_, columns=df.columns).round(1) 
print("\nCentroides SIN StandardScaler:") 
print(c_sin.sort_values("ingreso_mil").to_string(index=False)) 
print(f"Inercia sin escalar: {km_sin.inertia_:.2f}") 
  
# C) Caso extremo: ingreso en SOLES (valores miles de veces mayores que el gasto) 
d = pd.DataFrame({"ingreso_soles": df["ingreso_mil"] * 1000, 
                  "puntaje_gasto": df["puntaje_gasto"]}) 
km_s = KMeans(n_clusters=5, n_init=10, random_state=42).fit(d) 
c_s = pd.DataFrame(km_s.cluster_centers_, columns=d.columns).round(1) 
c_s["clientes"] = pd.Series(km_s.labels_).value_counts().sort_index().values 
print("\nSIN escalar, ingreso en soles:") 
print(c_s.sort_values("ingreso_soles").to_string(index=False)) 