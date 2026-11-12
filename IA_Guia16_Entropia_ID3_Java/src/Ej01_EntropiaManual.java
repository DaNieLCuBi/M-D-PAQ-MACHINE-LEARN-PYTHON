// Ej01_EntropiaManual.java - Verificación de los cálculos hechos a mano 
import java.util.Arrays; 
import java.util.Locale; 
  
public class Ej01_EntropiaManual { 
  
  static double entropia(int... conteos) { 
    int total = Arrays.stream(conteos).sum(); 
    double h = 0; 
    for (int c : conteos) { 
      if (c == 0) continue; 
      double p = (double) c / total; 
      h -= p * Math.log(p) / Math.log(2); 
    } 
    return h; 
  } 
  
  public static void main(String[] args) { 
    Locale.setDefault(Locale.US); 
    int[][] casos = {{6, 2}, {4, 4}, {3, 3, 2}}; 
    for (int[] c : casos) { 
      System.out.printf("%-10s -> H = %.3f bits%n", Arrays.toString(c), entropia(c)); 
    } 
  } 
} 