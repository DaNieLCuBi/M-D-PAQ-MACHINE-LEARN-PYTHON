// P04_Recorridos.java - Pre-order, in-order y post-order paso a paso
public class P04_Recorridos {

  static int paso;

  static void preOrden(Nodo<String> n, int nivel) {
    if (n == null) return;
    System.out.println("  ".repeat(nivel) + (++paso) + ") visita "
        + n.dato);  // 1° la raíz
    preOrden(n.izquierdo, nivel + 1);  // 2° izquierda
    preOrden(n.derecho, nivel + 1);  // 3° derecha
  }

  static void inOrden(Nodo<String> n, StringBuilder sb) {
    if (n == null) return;
    inOrden(n.izquierdo, sb);
    sb.append(n.dato).append(" ");
    inOrden(n.derecho, sb);
  }

  static void postOrden(Nodo<String> n, int nivel) {
    if (n == null) return;
    postOrden(n.izquierdo, nivel + 1);  // 1° izquierda
    postOrden(n.derecho, nivel + 1);  // 2° derecha
    System.out.println("  ".repeat(nivel) + (++paso) + ") visita "
        + n.dato); // 3° la raíz
  }

  public static void main(String[] args) {
    //            A
    //          /   \
    //         B     C
    //        / \   / \
    //       D   E F   G
    Nodo<String> arbol = new Nodo<>("A",
        new Nodo<>("B", new Nodo<>("D"), new Nodo<>("E")),
        new Nodo<>("C", new Nodo<>("F"), new Nodo<>("G")));

    System.out.println("PRE-ORDER (raíz, izquierda, derecha):");
    paso = 0;
    preOrden(arbol, 0);

    StringBuilder sb = new StringBuilder();
    inOrden(arbol, sb);
    System.out.println("\nIN-ORDER (izquierda, raíz, derecha): " + sb);

    System.out.println("\nPOST-ORDER (izquierda, derecha, raíz):");
    paso = 0;
    postOrden(arbol, 0);
  }
}
