# 03_tensores.py - Primeros pasos con TensorFlow: tensores y gradientes
import tensorflow as tf
 
print("Versión de TensorFlow:", tf.__version__)
 
# 1. Un tensor es un arreglo de n dimensiones (como un arreglo de NumPy)
vector = tf.constant([1.0, 2.0, 3.0])
print("Vector:", vector.numpy(), "| forma:", vector.shape, "| tipo:", vector.dtype)
 
a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
b = tf.constant([[5.0, 6.0], [7.0, 8.0]])
 
# 2. Operaciones con tensores
print("Suma:\n", (a + b).numpy())
print("Producto matricial:\n", tf.matmul(a, b).numpy())
print("Media de a:", tf.reduce_mean(a).numpy())
 
# 3. Variables: valores que la red modifica al aprender (pesos)
peso = tf.Variable(0.5)
peso.assign_add(0.25)
print("Peso actualizado:", peso.numpy())
 
# 4. GradientTape calcula derivadas automáticamente (base del aprendizaje)
x = tf.Variable(3.0)
with tf.GradientTape() as cinta:
    y = x ** 2 + 2 * x            # y = x² + 2x
derivada = cinta.gradient(y, x)   # dy/dx = 2x + 2
print("y en x=3:", y.numpy(), "| derivada:", derivada.numpy())
