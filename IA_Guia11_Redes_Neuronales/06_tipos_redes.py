# 06_tipos_redes.py - Estructura de los 4 tipos de redes neuronales en Keras 
from tensorflow import keras 
from tensorflow.keras import layers 
  
def describir(nombre, modelo): 
    print(f"--- {nombre} ---") 
    for capa in modelo.layers: 
        print(f"  {capa.__class__.__name__:<13} salida={str(capa.output.shape):<18} 
parámetros={capa.count_params()}") 
    print(f"  TOTAL: {modelo.count_params()} parámetros\n") 
  
# 1. FEEDFORWARD (FNN): datos tabulares, la información va en un solo sentido 
fnn = keras.Sequential([keras.Input(shape=(20,)), 
                        layers.Dense(16, activation="relu"), 
                        layers.Dense(1, activation="sigmoid")]) 
describir("Feedforward (FNN)", fnn) 
  
# 2. RECURRENTE (RNN): secuencias (texto, series de tiempo); recuerda lo anterior 
rnn = keras.Sequential([keras.Input(shape=(10, 1)),          # 10 pasos de tiempo, 1 
valor 
                        layers.SimpleRNN(16), 
                        layers.Dense(1)]) 
describir("Recurrente (RNN)", rnn) 
  
# 3. CONVOLUCIONAL (CNN): imágenes; los filtros detectan bordes y formas 
cnn = keras.Sequential([keras.Input(shape=(28, 28, 1)),      # imagen 28x28 en grises 
                        layers.Conv2D(8, (3, 3), activation="relu"), 
                        layers.MaxPooling2D((2, 2)), 
                        layers.Flatten(), 
                        layers.Dense(10, activation="softmax")]) 
describir("Convolucional (CNN)", cnn) 
  
# 4. GAN: dos redes que compiten (generador vs. discriminador) 
generador = keras.Sequential([keras.Input(shape=(16,)),       # ruido aleatorio 
                              layers.Dense(32, activation="relu"), 
                              layers.Dense(2)])               # dato "falso" de 2 
valores 
discriminador = keras.Sequential([keras.Input(shape=(2,)), 
                                  layers.Dense(32, activation="relu"), 
                                  layers.Dense(1, activation="sigmoid")])  # ¿real o 
falso? 
describir("GAN - Generador", generador) 
describir("GAN - Discriminador", discriminador) 