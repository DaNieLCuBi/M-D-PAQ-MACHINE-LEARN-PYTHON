# 01_tipos_no_supervisado.py - Los 3 tipos de aprendizaje no supervisado 
import numpy as np 
from sklearn.datasets import load_iris 
from sklearn.cluster import KMeans 
from sklearn.decomposition import PCA 
from sklearn.ensemble import IsolationForest 
  
X = load_iris().data          # SOLO las medidas: NO usamos las etiquetas (target) 
print("Datos sin etiquetas:", X.shape) 
  
# 1. AGRUPAMIENTO (Clustering): forma grupos de flores parecidas 
grupos = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X) 
print("\n1) Clustering -> flores por grupo:", np.bincount(grupos)) 
  
# 2. REDUCCIÓN DE LA DIMENSIONALIDAD: de 4 columnas a 2 
pca = PCA(n_components=2) 
X2 = pca.fit_transform(X) 
print("2) PCA -> forma nueva:", X2.shape, 
      "| información conservada:", f"{pca.explained_variance_ratio_.sum():.1%}") 
  
# 3. DETECCIÓN DE ANOMALÍAS: encuentra flores "raras" 
detector = IsolationForest(contamination=0.03, random_state=42) 
marcas = detector.fit_predict(X)                 # -1 = anomalía, 1 = normal 
print("3) Anomalías encontradas:", (marcas == -1).sum(), 
      "en las filas", np.where(marcas == -1)[0]) 