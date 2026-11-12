// P03_FlujoML.java - Flujo de trabajo del aprendizaje automático (REGRESIÓN)
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.Random;

public class P03_FlujoML {
  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Random azar = new Random(42);  // semilla: mismos datos en todas las PC

    // PASO 1. RECOLECTAR DATOS: horas de estudio (x) y nota obtenida (y)
    List<double[]> datos = new ArrayList<>();
    for (int i = 0; i < 30; i++) {
      double horas = Math.round((1 + 9 * azar.nextDouble()) * 10) / 10.0;
      double nota = 5 + 1.4 * horas + azar.nextGaussian() * 1.2;
      nota = Math.round(Math.min(20, Math.max(0, nota)) * 10) / 10.0;
      datos.add(new double[]{horas, nota});
    }
    System.out.println("PASO 1. Datos recolectados: " + datos.size() + " estudiantes");

    // PASO 2. PREPARAR: mezclar y dividir 80 % entrenamiento / 20 % prueba
    Collections.shuffle(datos, azar);
    int corte = (int) (datos.size() * 0.8);
    List<double[]> train = datos.subList(0, corte);
    List<double[]> test = datos.subList(corte, datos.size());
    System.out.println("PASO 2. Entrenamiento: " + train.size() + " | Prueba: "
        + test.size());

    // PASO 3. ENTRENAR: mínimos cuadrados  b1 = Σ(x-x̄)(y-ȳ) / Σ(x-x̄)²   b0 = ȳ -
    // b1·x̄
    double mx = 0, my = 0;
    for (double[] d : train) { mx += d[0]; my += d[1]; }
    mx /= train.size(); my /= train.size();
    double num = 0, den = 0;
    for (double[] d : train) {
      num += (d[0] - mx) * (d[1] - my);
      den += (d[0] - mx) * (d[0] - mx);
    }
    double b1 = num / den, b0 = my - b1 * mx;
    System.out.printf("PASO 3. Modelo aprendido: nota = %.3f + %.3f * horas%n", b0, b1);

    // PASO 4. EVALUAR con datos que el modelo NO vio
    double sumaErr = 0, ssRes = 0, ssTot = 0, myTest = 0;
    for (double[] d : test) myTest += d[1];
    myTest /= test.size();
    System.out.println("PASO 4. Evaluación con datos de prueba:");
    System.out.println("   horas  real  predicha");
    for (double[] d : test) {
      double pred = b0 + b1 * d[0];
      System.out.printf("   %5.1f %5.1f %9.2f%n", d[0], d[1], pred);
      sumaErr += Math.abs(d[1] - pred);
      ssRes += Math.pow(d[1] - pred, 2);
      ssTot += Math.pow(d[1] - myTest, 2);
    }
    System.out.printf("   MAE = %.3f puntos | R² = %.3f%n", sumaErr / test.size(),
        1 - ssRes / ssTot);

    // PASO 5. PREDECIR (usar el modelo con datos nuevos)
    double nuevas = 7.5;
    System.out.printf("PASO 5. Con %.1f horas de estudio la nota estimada es %.2f%n",
             nuevas, b0 + b1 * nuevas);
  }
}
