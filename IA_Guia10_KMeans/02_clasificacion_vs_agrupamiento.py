# 02_clasificacion_vs_agrupamiento.py - Mismo dataset, dos enfoques distintos 
import pandas as pd 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.cluster import KMeans 
  
iris = load_iris() 
X, y = iris.data, iris.target 
  
# CLASIFICACIÓN (supervisado): aprende de ejemplos CON etiqueta 
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0) 
arbol = DecisionTreeClassifier(random_state=0).fit(X_tr, y_tr) 
print("CLASIFICACIÓN (Árbol de decisión)") 
print("  ¿Usa etiquetas al entrenar?: Sí") 
print(f"  Exactitud en prueba: {arbol.score(X_te, y_te):.2%}") 
  
# AGRUPAMIENTO (no supervisado): descubre grupos SIN etiqueta 
km = KMeans(n_clusters=3, n_init=10, random_state=42).fit(X) 
print("\nAGRUPAMIENTO (K-Means)") 
print("  ¿Usa etiquetas al entrenar?: No") 
print("  Grupos descubiertos vs. especie real:") 
tabla = pd.crosstab(pd.Series(iris.target_names[y], name="especie_real"), 
                    pd.Series(km.labels_, name="grupo")) 
print(tabla)