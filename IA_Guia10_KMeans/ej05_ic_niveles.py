# ej05_ic_niveles.py - IC del 90 %, 95 % y 99 % para el gasto promedio de cada grupo 
import pandas as pd 
from scipy import stats 
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
  
df = pd.read_csv("clientes.csv") 
X = StandardScaler().fit_transform(df) 
df["grupo"] = KMeans(n_clusters=5, n_init=10, random_state=42).fit_predict(X) 
  
print("grupo nivel  media  lím_inf  lím_sup  ancho  t") 
for g, datos in df.groupby("grupo")["puntaje_gasto"]: 
    n = len(datos) 
    media = datos.mean() 
    ee = stats.sem(datos)                                   # s / raíz(n) 
    for nivel in (0.90, 0.95, 0.99): 
        li, ls = stats.t.interval(nivel, df=n - 1, loc=media, scale=ee) 
        t = stats.t.ppf((1 + nivel) / 2, n - 1)              # valor de la tabla t 
        print(f"{g:>4} {nivel:.0%} {media:>7.2f} {li:>8.2f} {ls:>8.2f} {ls - li:>6.2f} {t:.3f}")