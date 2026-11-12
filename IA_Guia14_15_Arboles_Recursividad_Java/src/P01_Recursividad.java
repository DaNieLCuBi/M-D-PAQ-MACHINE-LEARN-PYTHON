// P01_Recursividad.java - Funciones recursivas: caso base + caso recursivo
public class P01_Recursividad {

  // n! = n * (n-1)!     con     0! = 1
  static long factorial(int n, int nivel) {
    String sangria = "  ".repeat(nivel);
    System.out.println(sangria + "factorial(" + n + ") llamado");
    if (n <= 1) {                                         // CASO BASE: se detiene
      System.out.println(sangria + "factorial(" + n + ") = 1   <- caso base");
      return 1;
    }
    long resultado = n * factorial(n - 1, nivel + 1);     // CASO RECURSIVO
    System.out.println(sangria + "factorial(" + n + ") = " + resultado);
    return resultado;
  }

  // Suma de los dígitos: 4725 -> 4 + 7 + 2 + 5 = 18
  static int sumaDigitos(int n) {
    if (n < 10) return n;                     // caso base: un solo dígito
    return n % 10 + sumaDigitos(n / 10);      // último dígito + resto del número
  }

  // base^exp usando recursividad
  static long potencia(long base, int exp) {
    if (exp == 0) return 1;
    return base * potencia(base, exp - 1);
  }

  static int llamadas = 0;
  // Fibonacci: f(n) = f(n-1) + f(n-2)   con   f(0) = 0, f(1) = 1
  static long fibonacci(int n) {
    llamadas++;
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
  }

  public static void main(String[] args) {
    System.out.println("=== Traza de factorial(4) ===");
    System.out.println("Resultado final: " + factorial(4, 0));

    System.out.println("\nsumaDigitos(4725) = " + sumaDigitos(4725));
    System.out.println("potencia(2, 10)   = " + potencia(2, 10));

    System.out.println("\nSerie de Fibonacci:");
    for (int i = 0; i <= 10; i++) System.out.print(fibonacci(i) + " ");
    llamadas = 0;
    System.out.println("\nfibonacci(25) = " + fibonacci(25) + " necesitó " + llamadas
        + " llamadas");
  }
}
