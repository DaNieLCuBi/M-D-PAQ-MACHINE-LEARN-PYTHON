
# 01_scipy_estadistica.py - Estadística con scipy.stats
import numpy as np
import scipy
from scipy import stats
 
print("Versión de SciPy:", scipy.__version__)
 
# Notas de dos secciones de un mismo curso
seccion_a = np.array([14, 16, 13, 15, 17, 12, 15, 16, 14, 18])
seccion_b = np.array([12, 13, 11, 14, 12, 10, 13, 15, 11, 12])
 
# 1. Resumen estadístico
resumen = stats.describe(seccion_a)
print("Media A:", round(resumen.mean, 2), "| Varianza A:", round(resumen.variance, 2))
print("Moda de B:", stats.mode(seccion_b).mode)
 
# 2. Prueba t: ¿las dos secciones tienen promedios distintos?
t, p = stats.ttest_ind(seccion_a, seccion_b)
print(f"Estadístico t = {t:.3f} | valor p = {p:.4f}")
if p < 0.05:
    print("Conclusión: la diferencia de promedios es significativa (p < 0.05)")
else:
    print("Conclusión: no hay diferencia significativa")
 
# 3. Correlación de Pearson: horas de estudio vs. nota
horas = np.array([2, 3, 5, 6, 8, 9, 10])
notas = np.array([10, 11, 13, 14, 16, 17, 19])
r, p_r = stats.pearsonr(horas, notas)
print(f"Correlación r = {r:.3f} | valor p = {p_r:.6f}")
 
# 4. Distribución normal
normal = stats.norm(loc=14, scale=2)      # media 14, desviación 2
print("P(nota <= 12):", round(normal.cdf(12), 4))
print("P(nota >= 17):", round(1 - normal.cdf(17), 4))
