# 02_preprocesamiento.py - Grises, desenfoque, umbral y bordes 
import cv2 
import matplotlib.pyplot as plt 
  
img = cv2.imread("figuras.png") 
if img is None: 
    raise SystemExit("No se encontró figuras.png: ejecuta primero la Práctica 01") 
  
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)              # 1. escala de grises 
suave = cv2.GaussianBlur(gris, (5, 5), 0)                  # 2. quita ruido 
_, binaria = cv2.threshold(suave, 240, 255, cv2.THRESH_BINARY_INV)  # 3. objetos = 
blanco 
bordes = cv2.Canny(suave, 50, 150)                         # 4. detecta bordes 
  
print("Píxeles de objeto (umbral):", cv2.countNonZero(binaria)) 
print("Píxeles de borde (Canny)  :", cv2.countNonZero(bordes)) 
  
titulos = ["Original", "Grises", "Umbral (binaria)", "Bordes (Canny)"] 
imagenes = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB), gris, binaria, bordes] 
plt.figure(figsize=(10, 2.6)) 
for i in range(4): 
    plt.subplot(1, 4, i + 1) 
    plt.imshow(imagenes[i], cmap="gray") 
    plt.title(titulos[i]); plt.axis("off") 
plt.tight_layout() 
plt.savefig("g12_preproceso.png", dpi=110, bbox_inches="tight") 
plt.show() 