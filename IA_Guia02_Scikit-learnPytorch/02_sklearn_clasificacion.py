# 02_sklearn_clasificacion.py - Entrenar y evaluar un clasificador
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
 
X, y = load_iris(return_X_y=True)
 
# 1. Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
print("Entrenamiento:", X_train.shape, "| Prueba:", X_test.shape)
 
# 2. Escalar las características (media 0, desviación 1)
escalador = StandardScaler()
X_train_esc = escalador.fit_transform(X_train)   # aprende y transforma
X_test_esc = escalador.transform(X_test)         # solo transforma
 
# 3. Crear y entrenar el modelo
modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_train_esc, y_train)
 
# 4. Predecir y evaluar
y_pred = modelo.predict(X_test_esc)
print("Exactitud (accuracy):", round(accuracy_score(y_test, y_pred), 3))
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred,
      target_names=["setosa", "versicolor", "virginica"]))
 
# 5. Predecir una flor nueva
flor_nueva = [[5.1, 3.5, 1.4, 0.2]]
pred = modelo.predict(escalador.transform(flor_nueva))
print("Especie predicha para la flor nueva:", pred[0])
