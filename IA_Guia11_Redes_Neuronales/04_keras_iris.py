# 04_keras_iris.py - Mi primera red neuronal con TensorFlow y Keras 
import numpy as np 
from tensorflow import keras 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
  
keras.utils.set_random_seed(42)            # resultados repetibles 
  
# 1. DATOS: 150 flores, 4 medidas, 3 especies 
X, y = load_iris(return_X_y=True) 
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, 
stratify=y) 
escalador = StandardScaler() 
X_tr = escalador.fit_transform(X_tr) 
X_te = escalador.transform(X_te) 
  
# 2. ESTRUCTURA: entrada(4) -> oculta(10) -> oculta(8) -> salida(3) 
modelo = keras.Sequential([ 
    keras.Input(shape=(4,)), 
    keras.layers.Dense(10, activation="relu", name="oculta_1"), 
    keras.layers.Dense(8, activation="relu", name="oculta_2"), 
    keras.layers.Dense(3, activation="softmax", name="salida"), 
]) 
for capa in modelo.layers: 
    print(f"{capa.name:<9} neuronas={capa.units:<3} 
activación={capa.activation.__name__:<8} parámetros={capa.count_params()}") 
print("Total de parámetros:", modelo.count_params()) 
  
# 3. COMPILAR: optimizador, función de pérdida y métrica 
modelo.compile(optimizer="adam", loss="sparse_categorical_crossentropy", 
metrics=["accuracy"]) 
  
# 4. ENTRENAR 
hist = modelo.fit(X_tr, y_tr, epochs=100, batch_size=8, verbose=0) 
for ep in [1, 25, 50, 100]: 
    print(f"Época {ep:>3}: pérdida = {hist.history['loss'][ep-1]:.4f} | exactitud = 
{hist.history['accuracy'][ep-1]:.4f}") 
  
# 5. EVALUAR con datos de prueba 
perdida, exactitud = modelo.evaluate(X_te, y_te, verbose=0) 
print(f"Exactitud en prueba: {exactitud:.2%}") 
  
# 6. PREDECIR una flor nueva 
nueva = escalador.transform([[6.3, 2.9, 5.6, 1.8]]) 
prob = modelo.predict(nueva, verbose=0)[0] 
especies = ["setosa", "versicolor", "virginica"] 
print("Probabilidades:", {e: round(float(p), 3) for e, p in zip(especies, prob)}) 
print("Especie predicha:", especies[np.argmax(prob)]) 
  
modelo.save("modelo_iris.keras") 
print("Modelo guardado en modelo_iris.keras")