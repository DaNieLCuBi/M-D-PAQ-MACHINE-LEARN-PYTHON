// P04_ProyectoCreditos.java - PROYECTO: sistema que aprueba créditos con ID3
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.Random;
import java.util.Scanner;

public class P04_ProyectoCreditos {
  public static void main(String[] args) throws IOException {
    Locale.setDefault(Locale.US);
    Datos todos = Datos.cargarCSV("datos/creditos.csv");
    System.out.println("=== EVALUADOR DE CRÉDITOS (ID3) ===");
    System.out.println("Solicitudes históricas: " + todos.filas.size());

    // 1. Dividir: 75 % entrenamiento, 25 % prueba (semilla fija)
    List<String[]> filas = new ArrayList<>(todos.filas);
    Collections.shuffle(filas, new Random(7));
    int corte = (int) (filas.size() * 0.75);
    Datos train = new Datos(todos.atributos, todos.nombreClase, filas.subList(0,
        corte));
    List<String[]> test = filas.subList(corte, filas.size());
    System.out.println("Entrenamiento: " + train.filas.size() + " | Prueba: "
        + test.size());

    // 2. Entrenar el árbol
    ID3 id3 = new ID3(train);
    id3.entrenar();
    System.out.println("\nÁrbol aprendido:");
    id3.imprimir();

    // 3. Evaluar con datos que el árbol no vio
    int aciertos = 0;
    System.out.println("\nEvaluación:");
    for (String[] f : test) {
      String pred = id3.clasificar(f);
      String real = Datos.clase(f);
      if (pred.equals(real)) aciertos++;
      System.out.printf("  %-28s real=%-2s pred=%-2s %s%n",
          String.join(",", java.util.Arrays.copyOf(f, f.length - 1)),
          real, pred, pred.equals(real) ? "acierto" : "ERROR");
    }
    System.out.printf("Exactitud: %d/%d = %.1f %%%n", aciertos, test.size(),
        100.0 * aciertos / test.size());

    // 4. Usar el sistema con un cliente nuevo
    Scanner sc = new Scanner(System.in);
    String[] cliente = new String[todos.atributos.size()];
    String[][] opciones = {
        {"Alto", "Medio", "Bajo"}, {"Sí", "No"},
        {"Estable", "Temporal"}, {"Bueno", "Malo"}};
    System.out.println("\nNuevo cliente:");
    for (int i = 0; i < cliente.length; i++) {
      System.out.print("  " + todos.atributos.get(i) + " " + String.join("/",
          opciones[i]) + ": ");
      cliente[i] = sc.nextLine().trim();
    }
    System.out.println("DECISIÓN: " + (id3.clasificar(cliente).equals("Sí")
        ? "CRÉDITO APROBADO" : "CRÉDITO DENEGADO"));
  }
}
