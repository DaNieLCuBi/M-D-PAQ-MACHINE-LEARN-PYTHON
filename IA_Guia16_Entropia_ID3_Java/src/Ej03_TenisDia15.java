// Ej03_TenisDia15.java - ¿Qué pasa con el árbol si agregamos un día nuevo? 
import java.io.IOException; 
  
public class Ej03_TenisDia15 { 
  public static void main(String[] args) throws IOException { 
    Datos datos = Datos.cargarCSV("datos/jugar_tenis.csv"); 
    // Día 15: Nublado, Templado, Alta, Débil -> No 
    datos.filas.add(new String[]{"Nublado", "Templado", "Alta", "Débil", "No"}); 
    System.out.println("Días: " + datos.filas.size()); 
  
    ID3 id3 = new ID3(datos); 
    id3.mostrarPasos = true; 
    id3.entrenar(); 
    System.out.println("\nÁrbol con 15 días:"); 
    id3.imprimir(); 
    System.out.println("\nReglas:"); 
    id3.imprimirReglas(); 
  } 
} 