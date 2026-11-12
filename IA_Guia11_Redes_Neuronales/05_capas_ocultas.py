# 05_capas_ocultas.py - ¿Qué aportan las capas ocultas? (dataset de dos lunas) 
from tensorflow import keras 
from sklearn.datasets import make_moons 
from sklearn.model_selection import train_test_split 
  
X, y = make_moons(n_samples=500, noise=0.25, random_state=0) 
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0) 
  
def crear_red(ocultas): 
    capas = [keras.Input(shape=(2,))] 
    for n in ocultas: 
        capas.append(keras.layers.Dense(n, activation="relu")) 
    capas.append(keras.layers.Dense(1, activation="sigmoid"))     # salida binaria 
    return keras.Sequential(capas) 
  
configuraciones = {"Sin capas ocultas": [], "1 capa oculta (8)": [8], "2 capas ocultas 
(16, 8)": [16, 8]} 
print(f"{'Arquitectura':<25}{'Parámetros':>11}{'Exactitud':>11}") 
for nombre, ocultas in configuraciones.items(): 
    keras.utils.set_random_seed(0) 
    red = crear_red(ocultas) 
    red.compile(optimizer=keras.optimizers.Adam(0.01), loss="binary_crossentropy", 
metrics=["accuracy"]) 
    red.fit(X_tr, y_tr, epochs=150, batch_size=32, verbose=0) 
    _, acc = red.evaluate(X_te, y_te, verbose=0) 
    print(f"{nombre:<25}{red.count_params():>11}{acc:>11.2%}") 