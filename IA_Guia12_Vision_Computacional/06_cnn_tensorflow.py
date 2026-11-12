# 06_cnn_tensorflow.py - Clasificación de imágenes con una CNN en TensorFlow 
import numpy as np 
from tensorflow import keras 
from tensorflow.keras import layers 
from sklearn.datasets import load_digits 
from sklearn.model_selection import train_test_split 
  
keras.utils.set_random_seed(42) 
digitos = load_digits() 
X = digitos.images[..., np.newaxis] / 16.0               # (1797, 8, 8, 1) normalizado 
0 a 1 
X_tr, X_te, y_tr, y_te = train_test_split(X, digitos.target, test_size=0.25, 
random_state=42) 
  
cnn = keras.Sequential([ 
    keras.Input(shape=(8, 8, 1)), 
    layers.Conv2D(16, (3, 3), activation="relu"),        # 16 filtros detectan trazos 
    layers.MaxPooling2D((2, 2)),                         # reduce el tamaño 
    layers.Flatten(), 
    layers.Dense(10, activation="softmax"),              # 10 clases: dígitos 0 a 9 
]) 
cnn.compile(optimizer="adam", loss="sparse_categorical_crossentropy", 
metrics=["accuracy"]) 
print("Parámetros de la CNN:", cnn.count_params()) 
  
hist = cnn.fit(X_tr, y_tr, epochs=20, batch_size=32, validation_split=0.1, verbose=0) 
print(f"Exactitud entrenamiento (última época): {hist.history['accuracy'][-1]:.2%}") 
_, acc = cnn.evaluate(X_te, y_te, verbose=0) 
print(f"Exactitud en prueba: {acc:.2%}") 
  
prob = cnn.predict(X_te[:5], verbose=0) 
print("Predichos:", prob.argmax(axis=1), "| Reales:", y_te[:5]) 