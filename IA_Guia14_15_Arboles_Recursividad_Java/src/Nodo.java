// Nodo.java - Un nodo de árbol binario: un dato y dos enlaces (hijos)
public class Nodo<T> {
  T dato;
  Nodo<T> izquierdo;     // hijo izquierdo
  Nodo<T> derecho;       // hijo derecho

  public Nodo(T dato) {
    this.dato = dato;
  }

  public Nodo(T dato, Nodo<T> izquierdo, Nodo<T> derecho) {
    this.dato = dato;
    this.izquierdo = izquierdo;
    this.derecho = derecho;
  }

  public boolean esHoja() {
    return izquierdo == null && derecho == null;
  }
}
