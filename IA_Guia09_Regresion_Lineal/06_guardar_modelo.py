# 06_guardar_modelo.py - Guardar el modelo entrenado y reutilizarlo
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
 
df = pd.read_csv("estudiantes.csv")
modelo = LinearRegression().fit(df[["horas_estudio"]], df["nota"])
joblib.dump(modelo, "modelo_notas.pkl")            # se guarda en un archivo
print("Modelo guardado en modelo_notas.pkl")
 
modelo_cargado = joblib.load("modelo_notas.pkl")   # se vuelve a cargar
horas = 7.5                                        # en clase: float(input("Horas: "))
nota = modelo_cargado.predict(pd.DataFrame({"horas_estudio": [horas]}))[0]
print(f"Con {horas} horas de estudio, la nota estimada es {nota:.2f}")
print("¿Aprueba (nota >= 10.5)?", "Sí" if nota >= 10.5 else "No")
