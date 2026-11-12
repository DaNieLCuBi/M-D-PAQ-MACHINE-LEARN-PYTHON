# 05_nltk_sentimiento.py - Clasificador de opiniones con Naive Bayes de NLTK
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
 
vacias = set(stopwords.words("spanish"))
 
def extraer_caracteristicas(frase):
    """Convierte una frase en un diccionario {palabra: True}."""
    tokens = word_tokenize(frase.lower(), language="spanish")
    return {t: True for t in tokens if t.isalpha() and t not in vacias}
 
# Datos de entrenamiento: opiniones de estudiantes sobre un taller
datos = [
    ("El taller fue excelente y muy práctico", "positivo"),
    ("Me gustó mucho, el instructor explica muy bien", "positivo"),
    ("Aprendí bastante, las prácticas son útiles", "positivo"),
    ("Excelente contenido, muy recomendable", "positivo"),
    ("El curso es interesante y divertido", "positivo"),
    ("El taller fue aburrido y muy largo", "negativo"),
    ("No me gustó, la explicación fue confusa", "negativo"),
    ("Las prácticas son difíciles y poco útiles", "negativo"),
    ("Pésimo contenido, no lo recomiendo", "negativo"),
    ("El curso es lento y aburrido", "negativo"),
]
 
conjunto = [(extraer_caracteristicas(frase), etiqueta) for frase, etiqueta in datos]
 
# Entrenar el clasificador
clasificador = nltk.NaiveBayesClassifier.train(conjunto)
 
# Probar con frases nuevas
pruebas = [
    "Un taller muy práctico y excelente",
    "La clase fue aburrida y confusa",
    "Recomendable, el curso es divertido y práctico",
]
for frase in pruebas:
    resultado = clasificador.classify(extraer_caracteristicas(frase))
    print(f"'{frase}' -> {resultado}")
 
print("Exactitud en entrenamiento:", nltk.classify.accuracy(clasificador, conjunto))
clasificador.show_most_informative_features(5)
