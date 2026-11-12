# ej03_activaciones.py - Comparar relu, tanh y sigmoid en la red de la Práctica 04 
from tensorflow import keras 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
  
X, y = load_iris(return_X_y=True) 
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, 
stratify=y) 
esc = StandardScaler() 
X_tr, X_te = esc.fit_transform(X_tr), esc.transform(X_te) 
  
print(f"{'Activación':<10}{'Pérdida época 25':>18}{'Pérdida final':>15}{'Exactitud 
prueba':>18}") 
for act in ["relu", "tanh", "sigmoid"]: 
    keras.utils.set_random_seed(42) 
    modelo = keras.Sequential([ 
        keras.Input(shape=(4,)), 
        keras.layers.Dense(10, activation=act), 
        keras.layers.Dense(8, activation=act), 
        keras.layers.Dense(3, activation="softmax"), 
    ]) 
    modelo.compile(optimizer="adam", loss="sparse_categorical_crossentropy", 
metrics=["accuracy"]) 
    h = modelo.fit(X_tr, y_tr, epochs=100, batch_size=8, verbose=0) 
    _, acc = modelo.evaluate(X_te, y_te, verbose=0) 
    print(f"{act:<10}{h.history['loss'][24]:>18.4f}{h.history['loss'][-
1]:>15.4f}{acc:>18.2%}") 