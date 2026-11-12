// P03_ID3Tenis.java - Crear un árbol ID3 y usarlo para predecir
import java.io.IOException;

public class P03_ID3Tenis {
  public static void main(String[] args) throws IOException {
    Datos datos = Datos.cargarCSV("datos/jugar_tenis.csv");
    System.out.println("Datos: " + datos.filas.size() + " días | Atributos: "
        + datos.atributos);

    ID3 id3 = new ID3(datos);
    id3.mostrarPasos = true;  // muestra cómo decide en cada nivel
    System.out.println("\n--- Construcción del árbol ---");
    id3.entrenar();

    System.out.println("\n--- Árbol de decisión obtenido ---");
    id3.imprimir();

    System.out.println("\n--- Reglas SI ... ENTONCES ---");
    id3.imprimirReglas();

    System.out.println("\n--- Predicción de días nuevos ---");
    String[][] nuevos = {
      {"Soleado", "Frío", "Alta", "Fuerte"},
      {"Lluvioso", "Caluroso", "Normal", "Débil"},
      {"Nublado", "Frío", "Alta", "Fuerte"},
    };
    for (String[] dia : nuevos) {
      System.out.println(String.join(", ", dia) + "  ->  ¿Jugar? "
          + id3.clasificar(dia));
    }
  }
}
