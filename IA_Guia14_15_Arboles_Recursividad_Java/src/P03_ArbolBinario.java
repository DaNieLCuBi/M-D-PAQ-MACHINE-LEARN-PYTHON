// P03_ArbolBinario.java - Crear y consultar un árbol binario de búsqueda
public class P03_ArbolBinario {
  public static void main(String[] args) {
    ArbolBinario arbol = new ArbolBinario();
    int[] valores = {50, 30, 70, 20, 40, 60, 80, 35};
    System.out.print("Insertando: ");
    for (int v : valores) {
      System.out.print(v + " ");
      arbol.insertar(v);
    }
    System.out.println("\n\nÁrbol (gíralo 90° a la derecha para verlo de pie):");
    arbol.imprimir();

    System.out.println("\nNodos totales : " + arbol.contarNodos());
    System.out.println("Hojas         : " + arbol.contarHojas());
    System.out.println("Altura        : " + arbol.altura());
    System.out.println("¿Existe el 40?: " + arbol.buscar(40));
    System.out.println("¿Existe el 45?: " + arbol.buscar(45));
    System.out.println("Pre-orden : " + arbol.preOrden());
    System.out.println("In-orden  : " + arbol.inOrden() + "  <- sale ORDENADO");
    System.out.println("Post-orden: " + arbol.postOrden());
  }
}
