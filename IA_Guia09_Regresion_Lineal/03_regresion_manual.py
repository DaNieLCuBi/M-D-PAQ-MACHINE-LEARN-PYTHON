import pandas as pd

# 1. Cargar datos desde el CSV
df = pd.read_csv("estudiantes.csv")
x = df["horas_estudio"]
y = df["nota"]

# 2. Calcular promedios
x_media = x.mean()
y_media = y.mean()

# 3. Calcular Pendiente (b1) e Intercepto (b0)
b1 = ((x - x_media) * (y - y_media)).sum() / ((x - x_media) ** 2).sum()
b0 = y_media - (b1 * x_media)

# 4. Mostrar resultados
print(f"Pendiente   (b1): {b1:.4f}")
print(f"Intercepto  (b0): {b0:.4f}")
print(f"Ecuación: nota = {b0:.2f} + {b1:.2f} * horas")

# 5. Predicciones
for h in [2, 5, 8]:
    print(f"  Si estudia {h} h -> nota estimada = {b0 + b1 * h:.2f}")