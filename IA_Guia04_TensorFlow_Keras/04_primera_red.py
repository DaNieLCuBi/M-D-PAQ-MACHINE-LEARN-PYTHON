# 04_primera_red.py - La red más simple: aprender la regla y = 2x + 1
import numpy as np
import keras
from keras import layers
 
keras.utils.set_random_seed(42)          # resultados repetibles
 
# Datos de entrenamiento: la red NO conoce la fórmula, solo ve ejemplos
X = np.arange(-5, 6, dtype="float32")    # -5, -4, ..., 5
y = 2 * X + 1
print("x:", X)
print("y:", y)
 
# Modelo: 1 entrada -> 1 neurona (sin activación = salida lineal)
modelo = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(1),
])
modelo.compile(optimizer=keras.optimizers.SGD(learning_rate=0.01), loss="mse")
 
# Entrenamiento: 500 épocas (vueltas completas sobre los datos)
historial = modelo.fit(X, y, epochs=500, verbose=0)
for epoca in [1, 100, 250, 500]:
    print(f"Época {epoca:3}: pérdida (MSE) = {historial.history['loss'][epoca - 1]:.4f}")
 
# ¿Qué aprendió?
w, b = modelo.layers[0].get_weights()
print(f"Peso aprendido: {w[0][0]:.3f} (ideal 2) | Sesgo aprendido: {b[0]:.3f} (ideal 1)")
prediccion = modelo.predict(np.array([[10.0]]), verbose=0)
print(f"Predicción para x = 10: {prediccion[0][0]:.2f} (valor real 21)")
