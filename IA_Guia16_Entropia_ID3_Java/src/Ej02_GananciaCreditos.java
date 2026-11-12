// Ej02_GananciaCreditos.java - Ganancia de información de creditos.csv (24 filas) 
import java.io.IOException; 
import java.util.ArrayList; 
import java.util.List; 
import java.util.Locale; 
import java.util.Map; 
import java.util.TreeMap; 
  
public class Ej02_GananciaCreditos { 
  public static void main(String[] args) throws IOException { 
    Locale.setDefault(Locale.US); 
    Datos d = Datos.cargarCSV("datos/creditos.csv"); 
    double hTotal = ID3.entropia(d.filas); 
    System.out.printf("Filas: %d | H(S) = %.3f%n%n", d.filas.size(), hTotal); 
  
    String mejor = null; 
    double mejorG = -1; 
    for (String atributo : d.atributos) { 
      int col = d.columna(atributo); 
      Map<String, List<String[]>> grupos = new TreeMap<>(); 
      for (String[] f : d.filas) { 
        grupos.computeIfAbsent(f[col], k -> new ArrayList<>()).add(f); 
      } 
      double hPond = 0; 
      StringBuilder detalle = new StringBuilder(); 
      for (var g : grupos.entrySet()) { 
        // Conteo de cada clase dentro del grupo (sirve para cualquier dataset) 
        Map<String, Integer> conteo = new TreeMap<>(); 
        for (String[] f : g.getValue()) conteo.merge(Datos.clase(f), 1, Integer::sum); 
        double h = ID3.entropia(g.getValue()); 
        hPond += (double) g.getValue().size() / d.filas.size() * h; 
        detalle.append(String.format("   %-9s %2d filas %s  H = %.3f%n", 
            g.getKey(), g.getValue().size(), conteo, h)); 
      } 
      double ganancia = hTotal - hPond; 
      System.out.printf("%s%n%s   Ganancia = %.3f%n%n", atributo, detalle, ganancia); 
      if (ganancia > mejorG) { mejorG = ganancia; mejor = atributo; } 
    } 
    System.out.printf("RAÍZ con las 24 filas: %s (ganancia = %.3f)%n", mejor, mejorG); 
  } 
} 