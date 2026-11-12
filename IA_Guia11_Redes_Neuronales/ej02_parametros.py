# ej02_parametros.py - Verificar con Keras los parámetros de la red 4-8-6-3 
from tensorflow import keras 
  
modelo = keras.Sequential([ 
    keras.Input(shape=(4,)), 
    keras.layers.Dense(8, activation="relu"), 
    keras.layers.Dense(6, activation="relu"), 
    keras.layers.Dense(3, activation="softmax"), 
]) 
for capa in modelo.layers: 
    print(f"{capa.name:<8} parámetros = {capa.count_params()}") 
print("Total de parámetros:", modelo.count_params()) 