# 06_pytorch_regresion.py - Entrenar una regresión lineal con nn.Linear
import torch
from torch import nn
 
torch.manual_seed(0)
 
# Datos: y = 2x + 1 con algo de ruido
X = torch.linspace(0, 10, 100).unsqueeze(1)     # forma (100, 1)
y = 2 * X + 1 + torch.randn(100, 1) * 0.5
 
modelo = nn.Linear(in_features=1, out_features=1)
funcion_perdida = nn.MSELoss()
optimizador = torch.optim.SGD(modelo.parameters(), lr=0.01)
 
# Bucle de entrenamiento
for epoca in range(1, 1001):
    y_pred = modelo(X)                    # 1. paso hacia adelante
    perdida = funcion_perdida(y_pred, y)  # 2. calcular error
    optimizador.zero_grad()               # 3. limpiar gradientes
    perdida.backward()                    # 4. retropropagación
    optimizador.step()                    # 5. actualizar pesos
    if epoca % 200 == 0:
        print(f"Época {epoca}: pérdida = {perdida.item():.4f}")
peso = modelo.weight.item()
sesgo = modelo.bias.item()
print(f"Modelo aprendido: y = {peso:.2f}x + {sesgo:.2f}")
