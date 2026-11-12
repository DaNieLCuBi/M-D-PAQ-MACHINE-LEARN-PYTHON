# 04_pandas_operaciones.py - Selección, filtros, columnas nuevas y agrupación
import pandas as pd
import numpy as np
 
df = pd.DataFrame({
    "alumno": ["Ana", "Luis", "Rosa", "Pedro", "Carla", "Jorge"],
    "carrera": ["Software", "Redes", "Software", "Redes", "Software", "Redes"],
    "nota1": [15, 12, 18, 10, 14, 16],
    "nota2": [17, 11, 16, 13, 12, 15],
})
 
# 1. Seleccionar columnas
print(df["alumno"].tolist())
print(df[["alumno", "nota1"]])
 
# 2. loc (por etiqueta) e iloc (por posición)
print(df.loc[0, "alumno"])          # fila 0, columna 'alumno'
print(df.iloc[1:3, 0:2])            # filas 1-2, columnas 0-1
 
# 3. Crear columnas calculadas
df["promedio"] = (df["nota1"] + df["nota2"]) / 2
df["estado"] = np.where(df["promedio"] >= 13, "Aprobado", "Desaprobado")
print(df)
 
# 4. Filtrar filas
print(df[df["promedio"] >= 15])
print(df[(df["carrera"] == "Redes") & (df["estado"] == "Aprobado")])
 
# 5. Ordenar
print(df.sort_values("promedio", ascending=False).head(3))
 
# 6. Agrupar y resumir
resumen = df.groupby("carrera")["promedio"].agg(["mean", "max", "count"])
print(resumen.round(2))
print(df["estado"].value_counts())
