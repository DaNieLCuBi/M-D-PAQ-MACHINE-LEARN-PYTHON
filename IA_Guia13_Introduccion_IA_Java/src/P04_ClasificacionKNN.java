// P04_ClasificacionKNN.java - Aprendizaje SUPERVISADO de CLASIFICACIÓN (k vecinos)
import java.util.Arrays;
import java.util.Comparator;
import java.util.Locale;

public class P04_ClasificacionKNN {

  // Datos ETIQUETADOS: peso (g), textura (1 = lisa ... 10 = rugosa) -> fruta
  static double[][] X = {
    {150, 2}, {170, 1}, {140, 3}, {160, 2}, {130, 2},      // manzanas
    {180, 8}, {200, 9}, {190, 7}, {210, 8}, {175, 9}       // naranjas
  };
  static String[] y = {"manzana", "manzana", "manzana", "manzana", "manzana",
            "naranja", "naranja", "naranja", "naranja", "naranja"};

  static double distancia(double[] a, double[] b) {
    // Distancia euclidiana; la textura se multiplica por 10 para que pese igual que el
    // peso
    double dPeso = a[0] - b[0];
    double dTextura = (a[1] - b[1]) * 10;
    return Math.sqrt(dPeso * dPeso + dTextura * dTextura);
  }

  static String clasificar(double[] nueva, int k) {
    Integer[] indices = new Integer[X.length];
    for (int i = 0; i < X.length; i++) indices[i] = i;
    Arrays.sort(indices, Comparator.comparingDouble(i -> distancia(nueva, X[i])));
    int votosManzana = 0;
    System.out.print("   vecinos más cercanos:");
    for (int j = 0; j < k; j++) {
      int i = indices[j];
      System.out.printf(" %s(%.1f)", y[i], distancia(nueva, X[i]));
      if (y[i].equals("manzana")) votosManzana++;
    }
    System.out.println();
    return (votosManzana > k / 2) ? "manzana" : "naranja";
  }

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    double[][] nuevas = {{155, 2}, {195, 8}, {172, 5}};
    for (double[] f : nuevas) {
      System.out.printf("Fruta nueva: peso=%.0f g, textura=%.0f%n", f[0], f[1]);
      System.out.println("   => CLASE PREDICHA: " + clasificar(f, 3));
    }
  }
}
