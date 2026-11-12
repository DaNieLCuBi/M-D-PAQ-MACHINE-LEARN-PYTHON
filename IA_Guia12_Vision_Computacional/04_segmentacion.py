# 04_segmentacion.py - Segmentación por color (HSV) y por agrupamiento (K-Means) 
import cv2 
import numpy as np 
  
img = cv2.imread("figuras.png") 
  
# A) SEGMENTACIÓN POR COLOR: aislar solo lo ROJO 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)               # H = tono, S = saturación, V 
= brillo 
mascara1 = cv2.inRange(hsv, (0, 120, 70), (10, 255, 255))      # el rojo está en ambos 
extremos de H 
mascara2 = cv2.inRange(hsv, (170, 120, 70), (180, 255, 255)) 
mascara_roja = mascara1 | mascara2 
solo_rojo = cv2.bitwise_and(img, img, mask=mascara_roja) 
print("Píxeles rojos:", cv2.countNonZero(mascara_roja)) 
cv2.imwrite("segmento_rojo.png", solo_rojo) 
  
# B) SEGMENTACIÓN CON K-MEANS: agrupa los píxeles en k colores (patrones) 
pixeles = img.reshape(-1, 3).astype(np.float32)          # 120 000 filas x 3 columnas 
(B, G, R) 
criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0) 
cv2.setRNGSeed(0) 
_, etiquetas, centros = cv2.kmeans(pixeles, 5, None, criterio, 5, 
cv2.KMEANS_PP_CENTERS) 
centros = centros.astype(np.uint8) 
conteo = np.bincount(etiquetas.flatten()) 
print("\nColores descubiertos por K-Means (B, G, R) y % de la imagen:") 
for c, n in sorted(zip(centros.tolist(), conteo), key=lambda t: -t[1]): 
    print(f"  {str(c):<16} {n / len(pixeles):>6.1%}") 
  
segmentada = centros[etiquetas.flatten()].reshape(img.shape) 
cv2.imwrite("segmentada_kmeans.png", segmentada) 
cv2.imshow("Solo rojo", solo_rojo) 
cv2.imshow("K-Means", segmentada) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 