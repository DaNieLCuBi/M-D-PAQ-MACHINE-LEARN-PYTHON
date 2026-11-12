# 06_scipy_nltk_similitud.py - Proyecto integrador: similitud entre textos
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from scipy.spatial.distance import cosine
 
vacias = set(stopwords.words("spanish"))
stemmer = SnowballStemmer("spanish")
 
def procesar(texto):
    """NLTK: tokeniza, quita stopwords y obtiene raíces."""
    tokens = word_tokenize(texto.lower(), language="spanish")
    return [stemmer.stem(t) for t in tokens if t.isalpha() and t not in vacias]
 
documentos = {
    "doc1": "Los modelos de inteligencia artificial aprenden de los datos.",
    "doc2": "La inteligencia artificial usa datos para entrenar modelos.",
    "doc3": "El mantenimiento de motores eléctricos requiere herramientas.",
}
 
procesados = {nombre: procesar(t) for nombre, t in documentos.items()}
vocabulario = sorted(set(p for lista in procesados.values() for p in lista))
print("Vocabulario:", vocabulario)
 
# Vector de conteo (bolsa de palabras) para cada documento
def vectorizar(lista):
    return np.array([lista.count(p) for p in vocabulario])
 
vectores = {nombre: vectorizar(lista) for nombre, lista in procesados.items()}
 
# SciPy: similitud del coseno = 1 - distancia del coseno
def similitud(a, b):
    return 1 - cosine(vectores[a], vectores[b])
 
print(f"Similitud doc1 - doc2: {similitud('doc1', 'doc2'):.3f}")
print(f"Similitud doc1 - doc3: {similitud('doc1', 'doc3'):.3f}")
print(f"Similitud doc2 - doc3: {similitud('doc2', 'doc3'):.3f}")
