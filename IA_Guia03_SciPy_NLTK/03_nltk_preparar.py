# 03_nltk_preparar.py - Descargar los recursos de NLTK (se ejecuta UNA sola vez)
import nltk
 
print("Versión de NLTK:", nltk.__version__)
recursos = ["punkt", "punkt_tab", "stopwords"]
for recurso in recursos:
    nltk.download(recurso)
print("Recursos descargados correctamente")
