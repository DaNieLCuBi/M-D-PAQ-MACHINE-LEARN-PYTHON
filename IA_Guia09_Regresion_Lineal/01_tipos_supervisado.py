# 01_tipos_supervisado.py - Clasificación vs. Regresión (aprendizaje supervisado)
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
 
# ---- 1. CLASIFICACIÓN: la salida es una CATEGORÍA ----
iris = load_iris()
X, y = iris.data, iris.target                  # y = especie (0, 1 o 2)
clasificador = KNeighborsClassifier(n_neighbors=3)
clasificador.fit(X, y)                          # aprende con datos ETIQUETADOS
flor_nueva = [[5.1, 3.5, 1.4, 0.2]]
especie = clasificador.predict(flor_nueva)[0]
print("CLASIFICACIÓN")
print("  Medidas de la flor:", flor_nueva[0])
print("  Especie predicha  :", iris.target_names[especie])
 
# ---- 2. REGRESIÓN: la salida es un NÚMERO continuo ----
horas = [[1], [2], [3], [4], [5]]               # entrada: horas de estudio
notas = [8, 10, 12, 14, 16]                     # salida: nota obtenida
regresor = LinearRegression()
regresor.fit(horas, notas)
print("\nREGRESIÓN")
print("  Horas de estudio  : 6")
print("  Nota predicha     :", round(regresor.predict([[6]])[0], 2))
