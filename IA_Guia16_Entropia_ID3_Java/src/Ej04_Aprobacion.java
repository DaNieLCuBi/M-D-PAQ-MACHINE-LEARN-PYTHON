// Ej04_Aprobacion.java - Árbol ID3 con un dataset propio: ¿el estudiante aprueba? 
import java.io.IOException; 
  
public class Ej04_Aprobacion { 
  public static void main(String[] args) throws IOException { 
    Datos datos = Datos.cargarCSV("datos/aprobacion.csv"); 
    System.out.println("Estudiantes: " + datos.filas.size() 
        + " | Atributos: " + datos.atributos); 
  
    ID3 id3 = new ID3(datos); 
    id3.mostrarPasos = true; 
    id3.entrenar(); 
    System.out.println("\nÁrbol de decisión:"); 
    id3.imprimir(); 
    System.out.println("\nReglas:"); 
    id3.imprimirReglas(); 
  
    String[][] nuevos = {{"Media", "Completas", "No"}, {"Baja", "Incompletas", "Sí"}}; 
    System.out.println("\nPredicciones:"); 
    for (String[] e : nuevos) { 
      System.out.println("  " + String.join(", ", e) 
          + " -> ¿Aprueba? " + id3.clasificar(e)); 
    } 
  } 
} 