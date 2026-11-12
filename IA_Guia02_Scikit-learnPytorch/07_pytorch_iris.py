# 07_pytorch_iris.py - Red neuronal (MLP) para clasificar Iris
import torch
from torch import nn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
 
torch.manual_seed(42)
 
# 1. Preparar datos con Scikit-learn
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
esc = StandardScaler()
X_train = esc.fit_transform(X_train)
X_test = esc.transform(X_test)
 
# 2. Convertir a tensores
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)
 
# 3. Definir la red neuronal
class RedIris(nn.Module):
    def __init__(self):
        super().__init__()
        self.capas = nn.Sequential(
            nn.Linear(4, 16),   # 4 entradas -> 16 neuronas
            nn.ReLU(),
            nn.Linear(16, 3),   # 16 neuronas -> 3 clases
        )
 
    def forward(self, x):
        return self.capas(x)
 
modelo = RedIris()
perdida_fn = nn.CrossEntropyLoss()
optimizador = torch.optim.Adam(modelo.parameters(), lr=0.01)
 
# 4. Entrenar
for epoca in range(1, 201):
    modelo.train()
    salida = modelo(X_train)
    perdida = perdida_fn(salida, y_train)
    optimizador.zero_grad()
    perdida.backward()
    optimizador.step()
    if epoca % 50 == 0:
        print(f"Época {epoca}: pérdida = {perdida.item():.4f}")
 
# 5. Evaluar
modelo.eval()
with torch.no_grad():
    predicciones = modelo(X_test).argmax(dim=1)
    exactitud = (predicciones == y_test).float().mean().item()
print(f"Exactitud en prueba: {exactitud:.3f}")
 
# 6. Guardar los pesos del modelo
torch.save(modelo.state_dict(), "red_iris.pth")
print("Pesos guardados en red_iris.pth")
