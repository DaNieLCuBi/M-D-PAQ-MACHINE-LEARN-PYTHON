// Datos.java - Carga un archivo CSV: la última columna es la CLASE (etiqueta)
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Datos {
  public final List<String> atributos;  // nombres de las columnas (sin la clase)
  public final String nombreClase;          // nombre de la última columna
  public final List<String[]> filas;  // cada fila: valores de atributos + clase

  public Datos(List<String> atributos, String nombreClase, List<String[]> filas) {
    this.atributos = atributos;
    this.nombreClase = nombreClase;
    this.filas = filas;
  }

  public static Datos cargarCSV(String ruta) throws IOException {
    List<String> lineas = Files.readAllLines(Path.of(ruta));
    String[] cabecera = lineas.get(0).trim().split(",");
    List<String[]> filas = new ArrayList<>();
    for (int i = 1; i < lineas.size(); i++) {
      if (lineas.get(i).isBlank()) continue;
      String[] f = lineas.get(i).trim().split(",");
      for (int j = 0; j < f.length; j++) f[j] = f[j].trim();
      filas.add(f);
    }
    List<String> atributos = new ArrayList<>(Arrays.asList(cabecera).subList(0,
        cabecera.length - 1));
    return new Datos(atributos, cabecera[cabecera.length - 1], filas);
  }

  public int columna(String atributo) {
    return atributos.indexOf(atributo);
  }

  public static String clase(String[] fila) {
    return fila[fila.length - 1];
  }
}
