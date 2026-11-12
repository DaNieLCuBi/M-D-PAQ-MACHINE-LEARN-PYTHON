# 02_preparar_datos.py - Preparación de datos para la regresión lineal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
np.random.seed(42)                               # misma "aleatoriedad" en todas las PC
horas = np.round(np.random.uniform(1, 10, 40), 1)
ruido = np.random.normal(0, 1.2, 40)
nota = np.clip(np.round(5 + 1.4 * horas + ruido, 1), 0, 20)
 
df = pd.DataFrame({"horas_estudio": horas, "nota": nota})
df.to_csv("estudiantes.csv", index=False)        # guardamos el dataset
 
print("Primeras filas:")
print(df.head())
print("\nTamaño del dataset:", df.shape)
print("Valores nulos por columna:")
print(df.isnull().sum())
print("\nEstadísticas descriptivas:")
print(df.describe().round(2))
print("\nCorrelación horas-nota:", round(df["horas_estudio"].corr(df["nota"]), 3))
 
plt.scatter(df["horas_estudio"], df["nota"], color="steelblue")
plt.title("Horas de estudio vs. Nota")
plt.xlabel("Horas de estudio")
plt.ylabel("Nota (0 a 20)")
plt.grid(alpha=0.3)
plt.savefig("g9_dispersion.png", dpi=110, bbox_inches="tight")
plt.show()
