# 02_activaciones.py - Funciones de activación más usadas 
import numpy as np 
import matplotlib.pyplot as plt 
  
def sigmoide(z): return 1 / (1 + np.exp(-z)) 
def tanh(z):     return np.tanh(z) 
def relu(z):     return np.maximum(0, z) 
def softmax(z): 
    e = np.exp(z - np.max(z)) 
    return e / e.sum() 
  
print("   z    sigmoide   tanh    ReLU") 
for z in [-3, -1, 0, 1, 3]: 
    print(f"{z:>4} {sigmoide(z):>9.3f} {tanh(z):>7.3f} {relu(z):>6.1f}") 
  
puntajes = np.array([2.0, 1.0, 0.1])          # salida "cruda" de 3 neuronas 
prob = softmax(puntajes) 
print("\nSoftmax de", puntajes, "->", prob.round(3), "| suma =", prob.sum().round(2)) 
  
z = np.linspace(-5, 5, 200) 
plt.figure(figsize=(9, 3)) 
for i, (nombre, f) in enumerate([("Sigmoide", sigmoide), ("Tanh", tanh), ("ReLU", 
relu)]): 
    plt.subplot(1, 3, i + 1) 
    plt.plot(z, f(z), linewidth=2) 
    plt.title(nombre); plt.grid(alpha=0.3); plt.axhline(0, color="gray", lw=0.8) 
plt.tight_layout() 
plt.savefig("g11_activaciones.png", dpi=110, bbox_inches="tight") 
plt.show()