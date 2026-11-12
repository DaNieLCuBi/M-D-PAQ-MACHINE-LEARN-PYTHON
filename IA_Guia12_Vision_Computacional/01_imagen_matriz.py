# 01_imagen_matriz.py - Una imagen es una matriz de números (OpenCV + NumPy) 
import cv2 
import numpy as np 
  
# Creamos una imagen de 300 x 400 píxeles con fondo blanco (B, G, R) 
img = np.full((300, 400, 3), 255, dtype=np.uint8) 
cv2.circle(img, (80, 90), 50, (0, 0, 255), -1)                         # círculo rojo 
cv2.rectangle(img, (180, 40), (280, 140), (255, 0, 0), -1)             # cuadrado azul 
triangulo = np.array([[330, 140], [390, 140], [360, 40]]) 
cv2.fillPoly(img, [triangulo], (0, 170, 0))                            # triángulo 
verde 
cv2.rectangle(img, (60, 190), (300, 260), (0, 220, 255), -1)           # rectángulo 
amarillo 
cv2.imwrite("figuras.png", img)                                        # se usa en las 
prácticas siguientes 
  
print("Forma de la matriz (alto, ancho, canales):", img.shape) 
print("Tipo de dato:", img.dtype, "| valores de 0 a 255") 
print("Total de píxeles:", img.shape[0] * img.shape[1]) 
print("Píxel (fila 90, col 80)  [B G R] =", img[90, 80], "-> rojo") 
print("Píxel (fila 90, col 230) [B G R] =", img[90, 230], "-> azul") 
print("Píxel (fila 10, col 10)  [B G R] =", img[10, 10], "-> blanco") 
  
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
print("Imagen en grises:", gris.shape, "| un solo canal") 
  
cv2.imshow("Figuras", img)          # abre una ventana 
cv2.waitKey(0)                      # espera que presiones una tecla 
cv2.destroyAllWindows() 