# 04_sklearn_regresion.py - Regresión lineal: predecir un valor numérico
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
 
# Datos simulados: horas de estudio vs. nota obtenida
rng = np.random.default_rng(0)
horas = rng.uniform(1, 10, size=50).reshape(-1, 1)
nota = 6 + 1.3 * horas.ravel() + rng.normal(0, 1, size=50)
 
X_train, X_test, y_train, y_test = train_test_split(horas, nota, test_size=0.2, random_state=0)
 
reg = LinearRegression()
reg.fit(X_train, y_train)
 
print("Pendiente (coef):", round(reg.coef_[0], 3))
print("Intercepto:", round(reg.intercept_, 3))
 
y_pred = reg.predict(X_test)
print("Error absoluto medio (MAE):", round(mean_absolute_error(y_test, y_pred), 3))
print("Coeficiente R2:", round(r2_score(y_test, y_pred), 3))
print("Nota estimada con 8 horas de estudio:", round(reg.predict([[8]])[0], 2))
