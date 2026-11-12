CLS# 04_regresion_sklearn.py - Regresión lineal simple con scikit-learn (flujo completo)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
 
# 1. PREPARACIÓN DE DATOSs
df = pd.read_csv("estudiantes.csv")
X = df[["horas_estudio"]]          # doble corchete: X debe ser 2D (tabla)
y = df["nota"]                     # y es 1D (columna)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print("Datos de entrenamiento:", len(X_train), "| Datos de prueba:", len(X_test))
 
# 2. ENTRENAMIENTO DEL MODELO
modelo = LinearRegression()
modelo.fit(X_train, y_train)
print(f"Pendiente  : {modelo.coef_[0]:.4f}")
print(f"Intercepto : {modelo.intercept_:.4f}")
 
# 3. REALIZACIÓN DE PREDICCIONES
y_pred = modelo.predict(X_test)
comparacion = pd.DataFrame({"horas": X_test["horas_estudio"].values,
                            "nota_real": y_test.values,
                            "nota_predicha": y_pred.round(2)})
print("\nComparación en datos de prueba:")
print(comparacion.to_string(index=False))
 
# 4. EVALUACIÓN DEL MODELO
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"\nMAE  (error absoluto medio): {mae:.3f}")
print(f"RMSE (raíz del error cuadr.): {rmse:.3f}")
print(f"R²   (coef. de determinación): {r2:.3f}")
 
# Gráfico: puntos reales y recta aprendida
plt.scatter(X_train, y_train, color="steelblue", label="Entrenamiento")
plt.scatter(X_test, y_test, color="orange", label="Prueba")
xs = pd.DataFrame({"horas_estudio": np.linspace(1, 10, 50)})
plt.plot(xs, modelo.predict(xs), color="red", linewidth=2, label="Recta de regresión")
plt.title("Regresión lineal simple: horas vs. nota")
plt.xlabel("Horas de estudio"); plt.ylabel("Nota")
plt.legend(); plt.grid(alpha=0.3)
plt.savefig("g9_recta.png", dpi=110, bbox_inches="tight")
plt.show()
