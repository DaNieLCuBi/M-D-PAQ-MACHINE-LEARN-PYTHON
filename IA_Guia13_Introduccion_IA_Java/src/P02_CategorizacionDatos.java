// P02_CategorizacionDatos.java - Tipos de datos que usa la IA
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

public class P02_CategorizacionDatos {

  // Dato CATEGÓRICO ORDINAL: las categorías tienen un orden
  enum NivelIngles { BASICO, INTERMEDIO, AVANZADO }

  // Cada registro (fila) describe a un estudiante con 6 atributos (columnas)
  record Estudiante(String nombre,        // identificador (no se usa para aprender)
           int edad,             // numérico DISCRETO (se cuenta)
           double estatura,      // numérico CONTINUO (se mide)
           String distrito,      // categórico NOMINAL (sin orden)
           NivelIngles ingles,   // categórico ORDINAL (con orden)
           boolean trabaja) { }  // BOOLEANO (sí / no)

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Estudiante[] datos = {
      new Estudiante("Ana",   19, 1.62, "Comas",       NivelIngles.INTERMEDIO, false),
      new Estudiante("Luis",  22, 1.75, "Los Olivos",  NivelIngles.BASICO,     true),
      new Estudiante("Rosa",  20, 1.58, "Comas",       NivelIngles.AVANZADO,   false),
      new Estudiante("Pedro", 25, 1.80, "Independencia", NivelIngles.BASICO,   true),
      new Estudiante("Carla", 21, 1.66, "Los Olivos",  NivelIngles.INTERMEDIO, true),
      new Estudiante("Jorge", 19, 1.70, "Comas",       NivelIngles.AVANZADO,   false),
    };

    System.out.println("Atributo   | Tipo de dato          | Operación válida");
    System.out.println("-----------+-----------------------+------------------------");
    System.out.println("edad       | Numérico discreto     | promedio, máximo");
    System.out.println("estatura   | Numérico continuo     | promedio, rango");
    System.out.println("distrito   | Categórico nominal    | contar frecuencias");
    System.out.println("ingles     | Categórico ordinal    | comparar (mayor/menor)");
    System.out.println("trabaja    | Booleano              | contar sí / no");

    // Numéricos: se pueden promediar
    double sumaEdad = 0, sumaEst = 0;
    for (Estudiante e : datos) { sumaEdad += e.edad(); sumaEst += e.estatura(); }
    System.out.printf("%nEdad promedio    : %.2f años%n", sumaEdad / datos.length);
    System.out.printf("Estatura promedio: %.2f m%n", sumaEst / datos.length);

    // Nominal: NO se promedia, se cuenta cuántas veces aparece cada categoría
    Map<String, Integer> frecuencia = new TreeMap<>();
    for (Estudiante e : datos) frecuencia.merge(e.distrito(), 1, Integer::sum);
    System.out.println("Estudiantes por distrito: " + frecuencia);

    // Ordinal: sí se puede comparar usando su posición (ordinal)
    System.out.print("Inglés intermedio o superior: ");
    for (Estudiante e : datos) {
      if (e.ingles().ordinal() >= NivelIngles.INTERMEDIO.ordinal()) {
        System.out.print(e.nombre() + " ");
      }
    }
    // Booleano: se cuentan los verdaderos
    long trabajan = java.util.Arrays.stream(datos).filter(Estudiante::trabaja).count();
    System.out.println("\nEstudiantes que trabajan: " + trabajan + " de "
        + datos.length);
  }
}
