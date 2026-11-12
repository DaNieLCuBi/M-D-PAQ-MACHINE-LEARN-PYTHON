# 01_sklearn_datos.py - Cargar y explorar un dataset de Scikit-learn
import sklearn
import pandas as pd
from sklearn.datasets import load_iris
 
print("Versión de scikit-learn:", sklearn.__version__)
 
iris = load_iris()
X = iris.data          # características (entradas)
y = iris.target        # etiquetas (salida a predecir)
 
print("Forma de X:", X.shape)
print("Características:", iris.feature_names)
print("Clases:", [str(n) for n in iris.target_names])
 
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
 
# Convertir a DataFrame para explorarlo con Pandas
df = pd.DataFrame(X, columns=iris.feature_names)
df["especie"] = [iris.target_names[i] for i in y]
print(df.head())
print(df["especie"].value_counts())
