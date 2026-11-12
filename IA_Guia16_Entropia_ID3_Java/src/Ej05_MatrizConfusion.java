// Ej05_MatrizConfusion.java - Matriz de confusión del evaluador de créditos 
import java.io.IOException; 
import java.util.ArrayList; 
import java.util.Collections; 
import java.util.List; 
import java.util.Locale; 
import java.util.Random; 
  
public class Ej05_MatrizConfusion { 
  public static void main(String[] args) throws IOException { 
    Locale.setDefault(Locale.US); 
    Datos todos = Datos.cargarCSV("datos/creditos.csv"); 
    List<String[]> filas = new ArrayList<>(todos.filas); 
    Collections.shuffle(filas, new Random(7));               // misma división de la P04 
    int corte = (int) (filas.size() * 0.75); 
    Datos train = new Datos(todos.atributos, todos.nombreClase, 
        filas.subList(0, corte)); 
    List<String[]> test = filas.subList(corte, filas.size()); 
  
    ID3 id3 = new ID3(train); 
    id3.entrenar(); 
  
    // Clase positiva = "Sí" (crédito aprobado) 
    int vp = 0, vn = 0, fp = 0, fn = 0; 
    for (String[] f : test) { 
      boolean real = Datos.clase(f).equals("Sí"); 
      boolean pred = id3.clasificar(f).equals("Sí"); 
      if (real && pred) vp++; 
      else if (!real && !pred) vn++; 
      else if (!real && pred) fp++; 
      else fn++; 
    } 
    System.out.println("                    Predicho: Sí   Predicho: No"); 
    System.out.printf("Real: Sí (aprobar)       VP = %d        FN = %d%n", vp, fn); 
    System.out.printf("Real: No (denegar)       FP = %d        VN = %d%n", fp, vn); 
  
    int total = vp + vn + fp + fn; 
    System.out.printf("%nExactitud = (VP + VN) / total = (%d + %d) / %d = %.1f %%%n", 
        vp, vn, total, 100.0 * (vp + vn) / total); 
    System.out.printf("Precisión = VP / (VP + FP)    = %d / %d = %.1f %%%n", 
        vp, vp + fp, 100.0 * vp / (vp + fp)); 
    System.out.printf("Recall    = VP / (VP + FN)    = %d / %d = %.1f %%%n", 
        vp, vp + fn, 100.0 * vp / (vp + fn)); 
  } 
} 