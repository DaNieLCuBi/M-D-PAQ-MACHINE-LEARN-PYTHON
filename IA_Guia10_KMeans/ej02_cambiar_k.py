# ej02_cambiar_k.py - Comparar k = 3, 5 y 7 en la segmentación de clientes 
import pandas as pd 
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score 
  
df = pd.read_csv("clientes.csv") 
esc = StandardScaler() 
X = esc.fit_transform(df) 
  
for k in (3, 5, 7): 
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X) 
    c = pd.DataFrame(esc.inverse_transform(km.cluster_centers_), columns=df.columns).round(1) 
    c["clientes"] = pd.Series(km.labels_).value_counts().sort_index().values 
    print(f"\n=== k = {k} | inercia {km.inertia_:.2f} | silueta {silhouette_score(X, 
km.labels_):.3f}") 
    print(c.sort_values(["ingreso_mil", "puntaje_gasto"]).to_string(index=False)) 