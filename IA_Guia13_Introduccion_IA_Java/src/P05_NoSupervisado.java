// P05_NoSupervisado.java - Aprendizaje NO SUPERVISADO: agrupar clientes (K-Means)
import java.util.Locale;

public class P05_NoSupervisado {
  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    // Datos SIN etiqueta: gasto mensual (S/) y visitas al mes de 10 clientes
    double[][] clientes = {
      {120, 2}, {150, 3}, {100, 1}, {130, 2}, {140, 3},
      {480, 9}, {520, 10}, {450, 8}, {500, 12}, {470, 9}
    };
    int k = 2;
    // Centroides iniciales: el primer cliente y el último
    double[][] centro = {clientes[0].clone(), clientes[clientes.length - 1].clone()};
    int[] grupo = new int[clientes.length];

    for (int it = 1; it <= 10; it++) {
      // ASIGNACIÓN: cada cliente va al centroide más cercano
      for (int i = 0; i < clientes.length; i++) {
        double d0 = dist(clientes[i], centro[0]), d1 = dist(clientes[i], centro[1]);
        grupo[i] = (d0 <= d1) ? 0 : 1;
      }
      // ACTUALIZACIÓN: cada centroide pasa al promedio de su grupo
      double[][] nuevo = new double[k][2];
      int[] n = new int[k];
      for (int i = 0; i < clientes.length; i++) {
        nuevo[grupo[i]][0] += clientes[i][0];
        nuevo[grupo[i]][1] += clientes[i][1];
        n[grupo[i]]++;
      }
      boolean cambio = false;
      for (int g = 0; g < k; g++) {
        nuevo[g][0] /= n[g]; nuevo[g][1] /= n[g];
        if (dist(nuevo[g], centro[g]) > 1e-9) cambio = true;
        centro[g] = nuevo[g];
      }
      System.out.printf("Iteración %d: centro0=(%.1f, %.1f) centro1=(%.1f, %.1f)%n",
          it, centro[0][0], centro[0][1], centro[1][0], centro[1][1]);
      if (!cambio) {
        System.out.println("Los centroides no cambiaron: CONVERGIÓ.");
        break;
      }
    }
    System.out.println("\nCliente  gasto  visitas  grupo");
    for (int i = 0; i < clientes.length; i++) {
      System.out.printf("  C%-2d  %7.0f  %6.0f  %5d%n", i + 1, clientes[i][0],
          clientes[i][1], grupo[i]);
    }
    System.out.println("\nEl algoritmo formó los grupos SIN conocer etiquetas.");
    System.out.println("Nosotros los interpretamos: "
        + "grupo 0 = ocasionales, grupo 1 = frecuentes.");
  }

  static double dist(double[] a, double[] b) {
    return Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2));
  }
}
