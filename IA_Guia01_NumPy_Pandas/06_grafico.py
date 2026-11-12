# 06_grafico.py - Visualizar los resultados con Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.DataFrame({
    "alumno": ["Ana", "Luis", "Rosa", "Pedro", "Carla", "Jorge"],
    "promedio": [16.0, 11.5, 17.0, 11.5, 13.0, 15.5],
})
 
colores = ["tab:green" if p >= 13 else "tab:red" for p in df["promedio"]]
plt.bar(df["alumno"], df["promedio"], color=colores)
plt.axhline(13, linestyle="--", color="gray", label="Nota mínima (13)")
plt.title("Promedio por alumno")
plt.ylabel("Promedio")
plt.legend()
plt.tight_layout()
plt.savefig("promedios.png")
plt.show()
