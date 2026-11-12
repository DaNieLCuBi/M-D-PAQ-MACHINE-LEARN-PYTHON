// P06_JuegoSiNo.java - PROYECTO: Juego Sí/No "Adivina el animal" que APRENDE
// Cada nodo interno es una PREGUNTA; cada hoja es una RESPUESTA (un animal).
// Respuesta "s" -> rama izquierda   |   respuesta "n" -> rama derecha
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class P06_JuegoSiNo {

  static final String ARCHIVO = "datos/animales.txt";
  static Scanner sc = new Scanner(System.in);

  // ---------- CARGAR el árbol desde el archivo (lectura en PRE-ORDER) ----------
  static Nodo<String> cargar(Iterator<String> lineas) {
    String linea = lineas.next();
    Nodo<String> n = new Nodo<>(linea.substring(2));
    if (linea.startsWith("P:")) {  // una pregunta siempre tiene 2 hijos
      n.izquierdo = cargar(lineas);
      n.derecho = cargar(lineas);
    }
    return n;
  }

  // ---------- GUARDAR el árbol en el archivo (escritura en PRE-ORDER) ----------
  static void guardar(Nodo<String> n, PrintWriter out) {
    if (n.esHoja()) {
      out.println("R:" + n.dato);
    } else {
      out.println("P:" + n.dato);
      guardar(n.izquierdo, out);
      guardar(n.derecho, out);
    }
  }

  // ---------- JUGAR: se baja por el árbol de forma recursiva ----------
  static void jugar(Nodo<String> n) {
    if (!n.esHoja()) {                                  // es una pregunta
      if (preguntar(n.dato)) jugar(n.izquierdo);
      else jugar(n.derecho);
      return;
    }
    if (preguntar("¿Es un(a) " + n.dato + "?")) {       // es una respuesta
      System.out.println("¡Adiviné!");
    } else {
      aprender(n);
    }
  }

  // ---------- APRENDER: la hoja se convierte en una nueva pregunta ----------
  static void aprender(Nodo<String> hoja) {
    System.out.print("Me rindo. ¿En qué animal pensabas? ");
    String nuevo = sc.nextLine().trim();
    System.out.print("Escribe una pregunta que diferencie a " + nuevo + " de "
        + hoja.dato + ": ");
    String pregunta = sc.nextLine().trim();
    boolean siParaNuevo = preguntar("Para " + nuevo + ", ¿la respuesta es sí?");
    Nodo<String> viejo = new Nodo<>(hoja.dato);
    Nodo<String> otro = new Nodo<>(nuevo);
    hoja.dato = pregunta;
    hoja.izquierdo = siParaNuevo ? otro : viejo;
    hoja.derecho = siParaNuevo ? viejo : otro;
    System.out.println("¡Gracias! Ya aprendí a reconocer: " + nuevo);
  }

  static boolean preguntar(String texto) {
    System.out.print(texto + " (s/n): ");
    String r = sc.nextLine().trim().toLowerCase();
    return r.startsWith("s");
  }

  // POST-ORDER: cuenta los animales (hojas) que el juego conoce
  static int contarAnimales(Nodo<String> n) {
    if (n.esHoja()) return 1;
    return contarAnimales(n.izquierdo) + contarAnimales(n.derecho);
  }

  public static void main(String[] args) throws IOException {
    List<String> lineas = Files.readAllLines(Path.of(ARCHIVO));
    Nodo<String> raiz = cargar(lineas.iterator());
    System.out.println("=== ADIVINA EL ANIMAL ===");
    System.out.println("Conozco " + contarAnimales(raiz)
        + " animales. Piensa en uno...");

    do {
      jugar(raiz);
    } while (preguntar("¿Jugamos otra vez?"));

    try (PrintWriter out = new PrintWriter(Files.newBufferedWriter(Path.of(ARCHIVO)))) {
      guardar(raiz, out);
    }
    System.out.println("Ahora conozco " + contarAnimales(raiz)
        + " animales. Árbol guardado en " + ARCHIVO);
  }
}
