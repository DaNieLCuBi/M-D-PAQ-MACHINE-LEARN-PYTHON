# 03_localizar_clasificar.py - Localización (dónde) y clasificación (qué) de objetos 
import cv2 
  
img = cv2.imread("figuras.png") 
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
_, binaria = cv2.threshold(gris, 240, 255, cv2.THRESH_BINARY_INV) 
  
# Contornos externos: cada contorno es un objeto 
contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
print("Objetos encontrados:", len(contornos)) 
  
def clasificar(c): 
    perimetro = cv2.arcLength(c, True) 
    vertices = cv2.approxPolyDP(c, 0.03 * perimetro, True)   # simplifica el contorno 
    n = len(vertices) 
    if n == 3: 
        return "triangulo" 
    if n == 4: 
        x, y, w, h = cv2.boundingRect(c) 
        return "cuadrado" if 0.9 <= w / h <= 1.1 else "rectangulo" 
    return "circulo" 
  
for c in sorted(contornos, key=lambda c: cv2.boundingRect(c)[0]): 
    x, y, w, h = cv2.boundingRect(c)                  # LOCALIZACIÓN: caja delimitadora 
    forma = clasificar(c)                             # CLASIFICACIÓN: qué es 
    print(f"{forma:<11} x={x:>3} y={y:>3} ancho={w:>3} alto={h:>3} 
área={cv2.contourArea(c):>8.1f}") 
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)    # DETECCIÓN = dónde + 
qué 
    cv2.putText(img, forma, (x, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1) 
  
cv2.imwrite("figuras_detectadas.png", img) 
cv2.imshow("Deteccion de objetos", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 