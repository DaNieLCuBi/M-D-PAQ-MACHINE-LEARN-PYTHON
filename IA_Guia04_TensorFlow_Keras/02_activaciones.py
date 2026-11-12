# 02_activaciones.py - Principales funciones de activación
import numpy as np
import matplotlib.pyplot as plt
 
z = np.linspace(-5, 5, 200)
 
sigmoide = 1 / (1 + np.exp(-z))
tanh = np.tanh(z)
relu = np.maximum(0, z)
leaky_relu = np.where(z > 0, z, 0.1 * z)
 
# Softmax: convierte puntajes en probabilidades que suman 1
puntajes = np.array([2.0, 1.0, 0.1])
softmax = np.exp(puntajes) / np.exp(puntajes).sum()
print("Puntajes:", puntajes)
print("Softmax :", softmax.round(3), "| suma =", softmax.sum().round(3))
 
valores = np.array([-2.0, 0.0, 2.0])
print("Para z =", valores)
print("  sigmoide:", (1 / (1 + np.exp(-valores))).round(3))
print("  tanh    :", np.tanh(valores).round(3))
print("  relu    :", np.maximum(0, valores))
 
fig, ejes = plt.subplots(1, 4, figsize=(13, 3))
for ax, y, titulo in zip(ejes, [sigmoide, tanh, relu, leaky_relu],
                         ["Sigmoide (0 a 1)", "Tanh (-1 a 1)", "ReLU", "Leaky ReLU"]):
    ax.plot(z, y, linewidth=2)
    ax.axhline(0, color="gray", linewidth=0.7)
    ax.axvline(0, color="gray", linewidth=0.7)
    ax.set_title(titulo)
    ax.grid(alpha=0.3)
fig.tight_layout()
plt.savefig("02_activaciones.png", dpi=100, bbox_inches="tight")
print("Imagen guardada: 02_activaciones.png")
plt.show()
