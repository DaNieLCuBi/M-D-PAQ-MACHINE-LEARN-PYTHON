# 03_sklearn_comparar.py - Comparar modelos con Pipeline y validación cruzada
from sklearn.datasets import load_iris
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import joblib
 
X, y = load_iris(return_X_y=True)
 
modelos = {
    "Regresión logística": make_pipeline(StandardScaler(), LogisticRegression(max_iter=200)),
    "Árbol de decisión": DecisionTreeClassifier(max_depth=3, random_state=42),
    "KNN (k=5)": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
}
 
# Validación cruzada de 5 particiones
for nombre, modelo in modelos.items():
    puntajes = cross_val_score(modelo, X, y, cv=5)
    print(f"{nombre:22s} -> promedio: {puntajes.mean():.3f}  (+/- {puntajes.std():.3f})")
 
# Entrenar el mejor modelo con todos los datos y guardarlo
mejor = modelos["Árbol de decisión"].fit(X, y)
joblib.dump(mejor, "modelo_iris.joblib")
print("Modelo guardado en modelo_iris.joblib")
 
# Cargar el modelo guardado y usarlo
cargado = joblib.load("modelo_iris.joblib")
print("Predicción con el modelo cargado:", cargado.predict([[6.7, 3.0, 5.2, 2.3]]))
