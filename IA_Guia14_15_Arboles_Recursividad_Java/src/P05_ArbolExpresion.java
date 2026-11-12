// P05_ArbolExpresion.java - Aplicación: árbol de una expresión aritmética
public class P05_ArbolExpresion {

  // Pre-order -> notación PREFIJA (polaca)
  static String prefija(Nodo<String> n) {
    if (n.esHoja()) return n.dato;
    return n.dato + " " + prefija(n.izquierdo) + " " + prefija(n.derecho);
  }

  // In-order -> notación INFIJA (la que usamos en matemáticas)
  static String infija(Nodo<String> n) {
    if (n.esHoja()) return n.dato;
    return "(" + infija(n.izquierdo) + " " + n.dato + " " + infija(n.derecho) + ")";
  }

  // Post-order -> notación POSTFIJA (la que usan las calculadoras y compiladores)
  static String postfija(Nodo<String> n) {
    if (n.esHoja()) return n.dato;
    return postfija(n.izquierdo) + " " + postfija(n.derecho) + " " + n.dato;
  }

  // EVALUAR también es post-order: primero se calculan los hijos y al final el operador
  static double evaluar(Nodo<String> n) {
    if (n.esHoja()) return Double.parseDouble(n.dato);
    double a = evaluar(n.izquierdo);
    double b = evaluar(n.derecho);
    double r = switch (n.dato) {
      case "+" -> a + b;
      case "-" -> a - b;
      case "*" -> a * b;
      case "/" -> a / b;
      default -> throw new IllegalArgumentException("Operador no válido: " + n.dato);
    };
    System.out.println("   calcula " + a + " " + n.dato + " " + b + " = " + r);
    return r;
  }

  public static void main(String[] args) {
    //              /
    //            /   \
    //           *     2
    //         /   \
    //        +     -
    //       / \   / \
    //      3   4 8   2
    Nodo<String> expr = new Nodo<>("/",
        new Nodo<>("*",
            new Nodo<>("+", new Nodo<>("3"), new Nodo<>("4")),
            new Nodo<>("-", new Nodo<>("8"), new Nodo<>("2"))),
        new Nodo<>("2"));

    System.out.println("Prefija  (pre-order) : " + prefija(expr));
    System.out.println("Infija   (in-order)  : " + infija(expr));
    System.out.println("Postfija (post-order): " + postfija(expr));
    System.out.println("\nEvaluación (post-order):");
    System.out.println("Resultado = " + evaluar(expr));
  }
}
