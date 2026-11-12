// P06_ProyectoTutorIA.java - PROYECTO: Tutor IA (regresión + clasificación con datos
// CSV)
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class P06_ProyectoTutorIA {

  record Registro(double horas, double asistencia, double nota, String resultado) { }

  // Lee el archivo CSV y convierte cada línea en un Registro
  static List<Registro> cargar(String ruta) throws IOException {
    List<Registro> lista = new ArrayList<>();
    List<String> lineas = Files.readAllLines(Path.of(ruta));
    for (int i = 1; i < lineas.size(); i++) {  // i = 1: saltamos la cabecera
      String[] c = lineas.get(i).split(",");
      lista.add(new Registro(Double.parseDouble(c[0]), Double.parseDouble(c[1]),
                 Double.parseDouble(c[2]), c[3].trim()));
    }
    return lista;
  }

  // REGRESIÓN: predice un NÚMERO (la nota) a partir de las horas
  static double[] entrenarRegresion(List<Registro> d) {
    double mx = 0, my = 0;
    for (Registro r : d) { mx += r.horas(); my += r.nota(); }
    mx /= d.size(); my /= d.size();
    double num = 0, den = 0;
    for (Registro r : d) {
      num += (r.horas() - mx) * (r.nota() - my);
      den += (r.horas() - mx) * (r.horas() - mx);
    }
    double b1 = num / den;
    return new double[]{my - b1 * mx, b1};
  }

  // CLASIFICACIÓN: predice una CATEGORÍA (APRUEBA / DESAPRUEBA) con k = 3 vecinos
  static String clasificar(List<Registro> d, double horas, double asistencia) {
    List<Registro> orden = new ArrayList<>(d);
    // Escalamos: horas de 0 a 10 y asistencia de 0 a 100 -> ambas de 0 a 1
    orden.sort((a, b) -> Double.compare(dist(a, horas, asistencia), dist(b, horas,
        asistencia)));
    int aprueba = 0;
    for (int i = 0; i < 3; i++) {
      if (orden.get(i).resultado().equals("APRUEBA")) aprueba++;
    }
    return aprueba >= 2 ? "APRUEBA" : "DESAPRUEBA";
  }

  static double dist(Registro r, double h, double a) {
    return Math.hypot((r.horas() - h) / 10.0, (r.asistencia() - a) / 100.0);
  }

  public static void main(String[] args) throws IOException {
    Locale.setDefault(Locale.US);
    List<Registro> datos = cargar("datos/estudiantes.csv");
    System.out.println("=== TUTOR IA - SENATI ===");
    System.out.println("Registros cargados: " + datos.size());

    double[] modelo = entrenarRegresion(datos);
    System.out.printf("Modelo de regresión: nota = %.2f + %.2f * horas%n", modelo[0],
        modelo[1]);

    Scanner sc = new Scanner(System.in);
    System.out.print("Horas de estudio por semana: ");
    double horas = sc.nextDouble();
    System.out.print("Porcentaje de asistencia   : ");
    double asistencia = sc.nextDouble();

    double nota = modelo[0] + modelo[1] * horas;
    String resultado = clasificar(datos, horas, asistencia);
    System.out.printf("%n[Regresión]     Nota estimada : %.1f%n", nota);
    System.out.println("[Clasificación] Predicción    : " + resultado);
    if (resultado.equals("DESAPRUEBA")) {
      System.out.println("Consejo: aumenta tus horas de estudio y tu asistencia.");
    } else {
      System.out.println("¡Vas por buen camino! Mantén tu ritmo.");
    }
    sc.close();
  }
}
