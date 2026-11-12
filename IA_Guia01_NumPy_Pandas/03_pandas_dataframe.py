# 03_pandas_dataframe.py - Series y DataFrames
import pandas as pd
 
print("Versión de Pandas:", pd.__version__)
 
# 1. Series: una columna con índice
edades = pd.Series([19, 21, 20, 23], index=["Ana", "Luis", "Rosa", "Pedro"])
print(edades)
print("Edad de Rosa:", edades["Rosa"])
 
# 2. DataFrame: tabla con filas y columnas
datos = {
    "alumno": ["Ana", "Luis", "Rosa", "Pedro", "Carla", "Jorge"],
    "carrera": ["Software", "Redes", "Software", "Redes", "Software", "Redes"],
    "nota1": [15, 12, 18, 10, 14, 16],
    "nota2": [17, 11, 16, 13, 12, 15],
}
df = pd.DataFrame(datos)
print(df)
 
# 3. Explorar el DataFrame
print("Filas y columnas:", df.shape)
print("Columnas:", list(df.columns))
print(df.head(3))
df.info()
print(df.describe())
