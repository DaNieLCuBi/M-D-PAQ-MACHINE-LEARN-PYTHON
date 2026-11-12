// NodoID3.java - Nodo de un árbol de decisión (puede tener VARIAS ramas)
import java.util.LinkedHashMap;
import java.util.Map;

public class NodoID3 {
  String atributo;  // pregunta del nodo (null si es hoja)
  String clase;                                      // respuesta, solo en las hojas
  String mayoria;  // clase más frecuente en este nodo
  Map<String, NodoID3> hijos = new LinkedHashMap<>(); // valor del atributo -> subárbol

  boolean esHoja() {
    return atributo == null;
  }
}
