// ArbolBinario.java - Árbol binario de búsqueda (ABB) con métodos recursivos
import java.util.ArrayList;
import java.util.List;

public class ArbolBinario {
  private Nodo<Integer> raiz;

  // INSERTAR: menores a la izquierda, mayores a la derecha
  public void insertar(int valor) {
    raiz = insertar(raiz, valor);
  }
  private Nodo<Integer> insertar(Nodo<Integer> n, int valor) {
    if (n == null) return new Nodo<>(valor);  // caso base: lugar vacío
    if (valor < n.dato) n.izquierdo = insertar(n.izquierdo, valor);
    else if (valor > n.dato) n.derecho = insertar(n.derecho, valor);
    return n;  // (los repetidos se ignoran)
  }

  public boolean buscar(int valor) { return buscar(raiz, valor); }
  private boolean buscar(Nodo<Integer> n, int valor) {
    if (n == null) return false;
    if (valor == n.dato) return true;
    return valor < n.dato ? buscar(n.izquierdo, valor) : buscar(n.derecho, valor);
  }

  public int contarNodos() { return contarNodos(raiz); }
  private int contarNodos(Nodo<Integer> n) {
    if (n == null) return 0;
    return 1 + contarNodos(n.izquierdo) + contarNodos(n.derecho);
  }

  public int contarHojas() { return contarHojas(raiz); }
  private int contarHojas(Nodo<Integer> n) {
    if (n == null) return 0;
    if (n.esHoja()) return 1;
    return contarHojas(n.izquierdo) + contarHojas(n.derecho);
  }

  // Altura = número de niveles del camino más largo desde la raíz
  public int altura() { return altura(raiz); }
  private int altura(Nodo<Integer> n) {
    if (n == null) return 0;
    return 1 + Math.max(altura(n.izquierdo), altura(n.derecho));
  }

  // RECORRIDOS (traversal)
  public List<Integer> preOrden() {
    List<Integer> lista = new ArrayList<>();
    preOrden(raiz, lista);
    return lista;
  }
  public List<Integer> inOrden() {
    List<Integer> lista = new ArrayList<>();
    inOrden(raiz, lista);
    return lista;
  }
  public List<Integer> postOrden() {
    List<Integer> lista = new ArrayList<>();
    postOrden(raiz, lista);
    return lista;
  }

  private void preOrden(Nodo<Integer> n, List<Integer> l) {   // RAÍZ - izq - der
    if (n == null) return;
    l.add(n.dato);
    preOrden(n.izquierdo, l);
    preOrden(n.derecho, l);
  }
  private void inOrden(Nodo<Integer> n, List<Integer> l) {    // izq - RAÍZ - der
    if (n == null) return;
    inOrden(n.izquierdo, l);
    l.add(n.dato);
    inOrden(n.derecho, l);
  }
  private void postOrden(Nodo<Integer> n, List<Integer> l) {  // izq - der - RAÍZ
    if (n == null) return;
    postOrden(n.izquierdo, l);
    postOrden(n.derecho, l);
    l.add(n.dato);
  }

  // Dibuja el árbol "acostado": la raíz a la izquierda, el hijo derecho arriba
  public void imprimir() { imprimir(raiz, 0); }
  private void imprimir(Nodo<Integer> n, int nivel) {
    if (n == null) return;
    imprimir(n.derecho, nivel + 1);
    System.out.println("      ".repeat(nivel) + "-> " + n.dato);
    imprimir(n.izquierdo, nivel + 1);
  }
}
