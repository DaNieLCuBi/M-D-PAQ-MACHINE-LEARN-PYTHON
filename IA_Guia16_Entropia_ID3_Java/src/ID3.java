// ID3.java - Algoritmo ID3 (Iterative Dichotomiser 3) de Ross Quinlan
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

public class ID3 {
  private final Datos datos;
  private NodoID3 raiz;
  public boolean mostrarPasos = false;

  public ID3(Datos datos) {
    this.datos = datos;
  }

  public NodoID3 entrenar() {
    raiz = construir(datos.filas, new ArrayList<>(datos.atributos), 0);
    return raiz;
  }

  // ===== Construcción RECURSIVA del árbol =====
  private NodoID3 construir(List<String[]> filas, List<String> atributos, int nivel) {
    NodoID3 nodo = new NodoID3();
    nodo.mayoria = claseMayoritaria(filas);

    // CASO BASE 1: todas las filas tienen la misma clase -> hoja pura
    if (entropia(filas) == 0) {
      nodo.clase = Datos.clase(filas.get(0));
      return nodo;
    }
    // CASO BASE 2: ya no quedan atributos -> hoja con la clase mayoritaria
    if (atributos.isEmpty()) {
      nodo.clase = nodo.mayoria;
      return nodo;
    }
    // PASO RECURSIVO: elegir el atributo con MAYOR ganancia de información
    String mejor = null;
    double mejorG = -1;
    for (String a : atributos) {
      double g = ganancia(filas, a);
      if (mostrarPasos) System.out.printf(Locale.US, "%sGanancia(%s) = %.3f%n",
          "   ".repeat(nivel), a, g);
      if (g > mejorG) { mejorG = g; mejor = a; }
    }
    if (mostrarPasos) System.out.println("   ".repeat(nivel) + "=> se elige: " + mejor);
    nodo.atributo = mejor;

    List<String> restantes = new ArrayList<>(atributos);
    restantes.remove(mejor);
    for (var g : separar(filas, mejor).entrySet()) {
      if (mostrarPasos) System.out.println("   ".repeat(nivel) + "Rama " + mejor
          + " = " + g.getKey()
                        + " (" + g.getValue().size() + " filas)");
      nodo.hijos.put(g.getKey(), construir(g.getValue(), restantes, nivel + 1));
    }
    return nodo;
  }

  // ===== Fórmulas =====
  public static double entropia(List<String[]> filas) {
    Map<String, Integer> conteo = new TreeMap<>();
    for (String[] f : filas) conteo.merge(Datos.clase(f), 1, Integer::sum);
    double h = 0;
    for (int c : conteo.values()) {
      double p = (double) c / filas.size();
      h -= p * Math.log(p) / Math.log(2);
    }
    return h;
  }

  public double ganancia(List<String[]> filas, String atributo) {
    double hPonderada = 0;
    for (List<String[]> grupo : separar(filas, atributo).values()) {
      hPonderada += (double) grupo.size() / filas.size() * entropia(grupo);
    }
    return entropia(filas) - hPonderada;
  }

  private Map<String, List<String[]>> separar(List<String[]> filas, String atributo) {
    int col = datos.columna(atributo);
    Map<String, List<String[]>> grupos = new TreeMap<>();
    for (String[] f : filas) grupos.computeIfAbsent(f[col],
        k -> new ArrayList<>()).add(f);
    return grupos;
  }

  private static String claseMayoritaria(List<String[]> filas) {
    Map<String, Integer> conteo = new TreeMap<>();
    for (String[] f : filas) conteo.merge(Datos.clase(f), 1, Integer::sum);
    return Collections.max(conteo.entrySet(), Map.Entry.comparingByValue()).getKey();
  }

  // ===== Clasificar un ejemplo nuevo: bajar por el árbol (recursivo) =====
  public String clasificar(String[] ejemplo) {
    return clasificar(raiz, ejemplo);
  }
  private String clasificar(NodoID3 n, String[] ejemplo) {
    if (n.esHoja()) return n.clase;
    String valor = ejemplo[datos.columna(n.atributo)];
    NodoID3 hijo = n.hijos.get(valor);
    if (hijo == null) return n.mayoria;  // valor nunca visto: usa la mayoría
    return clasificar(hijo, ejemplo);
  }

  // ===== Mostrar el árbol (recorrido PRE-ORDER) =====
  public void imprimir() {
    System.out.println("[" + raiz.atributo + "]");
    imprimir(raiz, "");
  }
  private void imprimir(NodoID3 n, String prefijo) {
    int i = 0;
    for (var e : n.hijos.entrySet()) {
      boolean ultimo = (++i == n.hijos.size());
      NodoID3 h = e.getValue();
      String texto = h.esHoja() ? "=> " + datos.nombreClase + ": "
          + h.clase.toUpperCase()
                   : "[" + h.atributo + "]";
      System.out.println(prefijo + (ultimo ? "└── " : "├── ") + e.getKey() + " "
          + texto);
      if (!h.esHoja()) imprimir(h, prefijo + (ultimo ? "    " : "│   "));
    }
  }

  // ===== Convertir el árbol en reglas SI ... ENTONCES =====
  public void imprimirReglas() {
    reglas(raiz, "");
  }
  private void reglas(NodoID3 n, String condicion) {
    if (n.esHoja()) {
      System.out.println("SI " + condicion + " ENTONCES " + datos.nombreClase + " = "
          + n.clase);
      return;
    }
    for (var e : n.hijos.entrySet()) {
      String c = n.atributo + " = " + e.getKey();
      reglas(e.getValue(), condicion.isEmpty() ? c : condicion + " Y " + c);
    }
  }
}
