# 05_elegir_k.py - ¿Cuántos grupos? Método del codo y coeficiente de silueta 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score 
  
df = pd.read_csv("clientes.csv") 
X = StandardScaler().fit_transform(df) 
  
inercias = [] 
print(" k   inercia   silueta") 
for k in range(2, 10): 
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X) 
    inercias.append(km.inertia_) 
    print(f"{k:>2} {km.inertia_:>9.2f} {silhouette_score(X, km.labels_):>9.3f}") 
  
plt.plot(range(2, 10), inercias, marker="o") 
plt.title("Método del codo") 
plt.xlabel("Número de grupos (k)"); plt.ylabel("Inercia") 
plt.grid(alpha=0.3) 
plt.savefig("g10_codo.png", dpi=110, bbox_inches="tight") 
plt.show() 