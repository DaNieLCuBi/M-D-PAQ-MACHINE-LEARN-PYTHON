# 05_pandas_archivos.py - Leer CSV, limpiar datos y exportar a Excel
import pandas as pd
import numpy as np
 
# 1. Crear un archivo CSV de ejemplo (simula datos reales)
ventas = pd.DataFrame({
    "fecha": ["2026-01-05", "2026-01-12", "2026-02-03", "2026-02-20", "2026-03-08", "2026-03-15"],
    "producto": ["Laptop", "Mouse", "Laptop", "Teclado", "Mouse", "Teclado"],
    "cantidad": [2, 10, np.nan, 5, 8, 4],
    "precio": [2500, 35, 2500, 80, 35, np.nan],
})
ventas.to_csv("ventas.csv", index=False)
print("Archivo ventas.csv creado")
 
# 2. Leer el CSV
df = pd.read_csv("ventas.csv", parse_dates=["fecha"])
print(df)
 
# 3. Detectar y tratar valores faltantes (NaN)
print("Valores faltantes por columna:")
print(df.isna().sum())
df["cantidad"] = df["cantidad"].fillna(df["cantidad"].median())
df["precio"] = df["precio"].fillna(df.groupby("producto")["precio"].transform("mean"))
print(df)
 
# 4. Columnas derivadas
df["total"] = df["cantidad"] * df["precio"]
df["mes"] = df["fecha"].dt.month
print(df)
 
# 5. Tabla resumen por mes y producto
tabla = df.pivot_table(values="total", index="mes", columns="producto",
                       aggfunc="sum", fill_value=0)
print(tabla)
 
# 6. Exportar resultados
df.to_excel("reporte_ventas.xlsx", index=False)
print("Reporte exportado a reporte_ventas.xlsx")
