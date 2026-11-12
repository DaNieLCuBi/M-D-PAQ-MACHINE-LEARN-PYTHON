// P01_Entropia.java - Entropía de la información: mide el DESORDEN de un conjunto
import java.util.Locale;

public class P01_Entropia {

  // H(S) = - Σ p_i · log2(p_i)
  static double entropia(int... conteos) {
    int total = 0;
    for (int c : conteos) total += c;
    double h = 0;
    for (int c : conteos) {
      if (c == 0) continue;                    // 0 · log2(0) se toma como 0
      double p = (double) c / total;
      h -= p * log2(p);
    }
    return h;
  }

  static double log2(double x) {
    return Math.log(x) / Math.log(2);  // Java no trae log2: se cambia de base
  }

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    int[][] casos = {{14, 0}, {13, 1}, {10, 4}, {9, 5}, {7, 7}, {5, 5, 5}};
    System.out.println("Conjunto (conteo por clase)   Entropía   Interpretación");
    for (int[] c : casos) {
      double h = entropia(c);
      String txt = (h == 0) ? "PURO: todos iguales"
           : (h >= 0.99 && c.length == 2) ? "MÁXIMO desorden (50/50)"
           : (c.length == 3) ? "3 clases iguales: máximo = log2(3)"
           : (h < 0.5) ? "casi puro" : "mezclado";
      System.out.printf("%-28s %8.3f   %s%n", java.util.Arrays.toString(c), h, txt);
    }

    System.out.println("\nCálculo paso a paso para [9 Sí, 5 No]:");
    double p1 = 9 / 14.0, p2 = 5 / 14.0;
    System.out.printf("  p(Sí) = 9/14 = %.4f   ->  -p·log2(p) = %.4f%n", p1,
        -p1 * log2(p1));
    System.out.printf("  p(No) = 5/14 = %.4f   ->  -p·log2(p) = %.4f%n", p2,
        -p2 * log2(p2));
    System.out.printf("  H(S)  = %.4f + %.4f = %.4f bits%n",
        -p1 * log2(p1), -p2 * log2(p2), entropia(9, 5));
  }
}
