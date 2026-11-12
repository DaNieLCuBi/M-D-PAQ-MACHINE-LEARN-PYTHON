// P02_GananciaInformacion.java - ¿Qué atributo separa MEJOR los datos?
import java.io.IOException;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

public class P02_GananciaInformacion {

  // Entropía de un grupo de filas según su clase (última columna)
  static double entropia(List<String[]> filas) {
    Map<String, Integer> conteo = new TreeMap<>();
    for (String[] f : filas) conteo.merge(Datos.clase(f), 1, Integer::sum);
    double h = 0;
    for (int c : conteo.values()) {
      double p = (double) c / filas.size();
      h -= p * Math.log(p) / Math.log(2);
    }
    return h;
  }

  public static void main(String[] args) throws IOException {
    Locale.setDefault(Locale.US);
    Datos d = Datos.cargarCSV("datos/jugar_tenis.csv");
    double hTotal = entropia(d.filas);
    System.out.printf("Entropía del conjunto completo H(S) = %.3f%n", hTotal);

    String mejor = null;
    double mejorGanancia = -1;
    for (String atributo : d.atributos) {
      int col = d.columna(atributo);
      // Separar las filas según el valor del atributo
      Map<String, List<String[]>> grupos = new TreeMap<>();
      for (String[] f : d.filas) {
        grupos.computeIfAbsent(f[col], k -> new java.util.ArrayList<>()).add(f);
      }
      System.out.println("\nAtributo: " + atributo);
      double hPonderada = 0;
      for (var g : grupos.entrySet()) {
        long si = g.getValue().stream()
            .filter(f -> Datos.clase(f).equals("Sí")).count();
        long no = g.getValue().size() - si;
        double h = entropia(g.getValue());
        double peso = (double) g.getValue().size() / d.filas.size();
        hPonderada += peso * h;
        System.out.printf("   %-9s %2d filas [%d Sí, %d No]  H = %.3f  peso = %d/14%n",
            g.getKey(), g.getValue().size(), si, no, h, g.getValue().size());
      }
      double ganancia = hTotal - hPonderada;
      System.out.printf("   Ganancia(%s) = %.3f - %.3f = %.3f%n", atributo, hTotal,
          hPonderada, ganancia);
      if (ganancia > mejorGanancia) { mejorGanancia = ganancia; mejor = atributo; }
    }
    System.out.printf("%nMEJOR ATRIBUTO para la raíz: %s (ganancia = %.3f)%n", mejor,
        mejorGanancia);
  }
}
