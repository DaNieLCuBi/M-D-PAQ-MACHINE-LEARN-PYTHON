# 05_clasificar_digitos.py - Machine Learning para clasificar imágenes de dígitos 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_digits 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score, confusion_matrix 
  
digitos = load_digits()                     # 1 797 imágenes de 8 x 8 píxeles (0 a 16) 
print("Imágenes:", digitos.images.shape, "| Etiquetas:", digitos.target.shape) 
print("Imagen 0 (matriz 8x8) -> dígito", digitos.target[0]) 
print(digitos.images[0].astype(int)) 
  
X = digitos.images.reshape(len(digitos.images), -1)    # cada imagen -> vector de 64 
valores 
X_tr, X_te, y_tr, y_te = train_test_split(X, digitos.target, test_size=0.25, 
random_state=42) 
  
modelo = SVC(gamma=0.001)                    # clasificador de máquina de soporte 
vectorial 
modelo.fit(X_tr, y_tr) 
pred = modelo.predict(X_te) 
print(f"\nExactitud en prueba: {accuracy_score(y_te, pred):.2%}") 
print("Matriz de confusión (filas = real, columnas = predicho):") 
print(confusion_matrix(y_te, pred)) 
  
plt.figure(figsize=(8, 2.2)) 
for i in range(6): 
    plt.subplot(1, 6, i + 1) 
    plt.imshow(X_te[i].reshape(8, 8), cmap="gray_r") 
    plt.title(f"Pred: {pred[i]}\nReal: {y_te[i]}", fontsize=9); plt.axis("off") 
plt.tight_layout() 
plt.savefig("g12_digitos.png", dpi=110, bbox_inches="tight") 
plt.show() 