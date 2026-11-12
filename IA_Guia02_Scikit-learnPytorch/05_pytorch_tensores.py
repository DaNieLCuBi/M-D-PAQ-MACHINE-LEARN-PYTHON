# 05_pytorch_tensores.py - Tensores y autograd en PyTorch
import torch
 
print("Versión de PyTorch:", torch.__version__)
dispositivo = "cuda" if torch.cuda.is_available() else "cpu"
print("Dispositivo disponible:", dispositivo)
 
# 1. Crear tensores
t1 = torch.tensor([1.0, 2.0, 3.0])
t2 = torch.zeros(2, 3)
t3 = torch.rand(2, 2)            # valores aleatorios entre 0 y 1
print(t1, t1.shape, t1.dtype)
print(t2)
 
# 2. Operaciones
a = torch.tensor([[1., 2.], [3., 4.]])
b = torch.tensor([[5., 6.], [7., 8.]])
print("Suma:\n", a + b)
print("Producto matricial:\n", a @ b)
print("Media de a:", a.mean().item())
 
# 3. Conversión entre NumPy y PyTorch
import numpy as np
arr = np.array([1, 2, 3])
t_desde_np = torch.from_numpy(arr)
print("De NumPy a tensor:", t_desde_np)
print("De tensor a NumPy:", t_desde_np.numpy())
 
# 4. Autograd: cálculo automático de derivadas
x = torch.tensor(3.0, requires_grad=True)
y = x ** 2 + 2 * x + 1          # y = x² + 2x + 1
y.backward()                     # calcula dy/dx
print("Derivada de y en x=3:", x.grad.item())   # 2x + 2 = 8
