# 05_regresion_multiple.py - Regresión lineal MÚLTIPLE: precio de departamentos
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
 
np.random.seed(7)
n = 120
area = np.random.randint(45, 160, n)             # m²
habitaciones = np.random.randint(1, 5, n)
antiguedad = np.random.randint(0, 30, n)         # años
precio = (2500 * area + 15000 * habitaciones - 1800 * antiguedad
          + 40000 + np.random.normal(0, 20000, n))  # soles
df = pd.DataFrame({"area": area, "habitaciones": habitaciones,
                   "antiguedad": antiguedad, "precio": precio.round(0)})
print(df.head())
 
X = df[["area", "habitaciones", "antiguedad"]]   # VARIAS variables de entrada
y = df["precio"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
 
modelo = LinearRegression().fit(X_train, y_train)
print("\nCoeficientes (cuánto cambia el precio por cada unidad):")
for nombre, coef in zip(X.columns, modelo.coef_):
    print(f"  {nombre:<13}: {coef:>10.2f}")
print(f"  Intercepto   : {modelo.intercept_:>10.2f}")
 
y_pred = modelo.predict(X_test)
print(f"\nR²  : {r2_score(y_test, y_pred):.3f}")
print(f"MAE : S/ {mean_absolute_error(y_test, y_pred):,.2f}")
 
nuevo = pd.DataFrame({"area": [90], "habitaciones": [3], "antiguedad": [10]})
print(f"\nDepartamento de 90 m², 3 hab., 10 años -> S/ {modelo.predict(nuevo)[0]:,.2f}")
