# 04_nltk_texto.py - Tokenizar, limpiar, lematizar raíces y contar palabras
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.probability import FreqDist
from nltk.util import ngrams


texto = ("La inteligencia artificial está transformando la industria. "
         "En SENATI aprendemos Python para crear modelos de inteligencia artificial. "
         "Los modelos aprenden patrones a partir de los datos.")

# 1. Dividir en oraciones
oraciones = sent_tokenize(texto, language="spanish")
print("Número de oraciones:", len(oraciones))
for i, o in enumerate(oraciones, start=1):
    print(f"  {i}. {o}")

# 2. Dividir en palabras (tokens)
tokens = word_tokenize(texto, language="spanish")
print("Primeros 10 tokens:", tokens[:10])

# 3. Normalizar: minúsculas y solo palabras (sin signos de puntuación)
palabras = [t.lower() for t in tokens if t.isalpha()]

# 4. Quitar palabras vacías (stopwords): la, de, en, los, para...
vacias = set(stopwords.words("spanish"))
utiles = [p for p in palabras if p not in vacias]
print("Palabras útiles:", utiles)

# 5. Stemming: reducir cada palabra a su raíz
stemmer = SnowballStemmer("spanish")
raices = [stemmer.stem(p) for p in utiles]
print("Raíces:", raices)

# 6. Frecuencia de palabras
frecuencia = FreqDist(utiles)
print("Palabras más frecuentes:", frecuencia.most_common(3))

# 7. Bigramas (pares de palabras consecutivas)
bigramas = list(ngrams(utiles, 2))
print("Primeros 3 bigramas:", bigramas[:3])

# 8. Mostrar el gráfico de frecuencias
frecuencia.plot(10)
plt.show()