// P02_RecursivoVsIterativo.java - Comparación y problemas clásicos de recursividad
public class P02_RecursivoVsIterativo {

  static long factorialIterativo(int n) {
    long r = 1;
    for (int i = 2; i <= n; i++) r *= i;          // usa un bucle
    return r;
  }

  static long factorialRecursivo(int n) {
    return (n <= 1) ? 1 : n * factorialRecursivo(n - 1);   // se llama a sí mismo
  }

  // Un texto es palíndromo si su primera y última letra son iguales
  // y el texto del medio también es palíndromo
  static boolean esPalindromo(String t) {
    if (t.length() <= 1) return true;                       // caso base
    if (t.charAt(0) != t.charAt(t.length() - 1)) return false;
    return esPalindromo(t.substring(1, t.length() - 1));    // reduce el problema
  }

  // Búsqueda binaria recursiva en un arreglo ORDENADO
  static int buscar(int[] a, int clave, int ini, int fin) {
    if (ini > fin) return -1;                               // caso base: no está
    int medio = (ini + fin) / 2;
    System.out.println("   revisando posiciones " + ini + " a " + fin + " -> medio = "
        + a[medio]);
    if (a[medio] == clave) return medio;                    // caso base: encontrado
    if (clave < a[medio]) return buscar(a, clave, ini, medio - 1);
    return buscar(a, clave, medio + 1, fin);
  }

  // ERROR TÍPICO: recursión SIN caso base
  static int sinCasoBase(int n) {
    return sinCasoBase(n + 1);
  }

  public static void main(String[] args) {
    System.out.println("factorial(10) iterativo = " + factorialIterativo(10));
    System.out.println("factorial(10) recursivo = " + factorialRecursivo(10));

    for (String p : new String[]{"reconocer", "anilina", "senati"}) {
      System.out.println("¿\"" + p + "\" es palíndromo? " + esPalindromo(p));
    }

    int[] notas = {5, 8, 10, 11, 13, 14, 16, 17, 19, 20};
    System.out.println("\nBuscando 16 en el arreglo ordenado:");
    System.out.println("   encontrado en la posición " + buscar(notas, 16, 0,
        notas.length - 1));

    try {
      sinCasoBase(1);
    } catch (StackOverflowError e) {
      System.out.println("\nsinCasoBase() provocó StackOverflowError: "
          + "la pila de llamadas se llenó.");
    }
  }
}
