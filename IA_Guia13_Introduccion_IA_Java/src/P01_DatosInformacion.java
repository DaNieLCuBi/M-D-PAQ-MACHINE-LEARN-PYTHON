// P01_DatosInformacion.java - De DATOS a INFORMACIÓN
import java.util.Locale;

public class P01_DatosInformacion {
  public static void main(String[] args) {
    Locale.setDefault(Locale.US);                  // punto decimal en todas las PC

    // 1. DATOS: hechos sin procesar (temperatura máxima de una semana, en °C)
    String[] dias = {"Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"};
    double[] temp = {19.5, 21.0, 22.4, 18.9, 23.1, 24.6, 20.2};

    System.out.println("DATOS (sin procesar):");
    for (int i = 0; i < dias.length; i++) {
      System.out.printf("  %s = %.1f%n", dias[i], temp[i]);
    }

    // 2. PROCESAMIENTO: calculamos, comparamos y contamos
    double suma = 0;
    int iMax = 0, iMin = 0, calurosos = 0;
    for (int i = 0; i < temp.length; i++) {
      suma += temp[i];
      if (temp[i] > temp[iMax]) iMax = i;
      if (temp[i] < temp[iMin]) iMin = i;
      if (temp[i] > 22) calurosos++;
    }
    double promedio = suma / temp.length;

    // 3. INFORMACIÓN: datos procesados que tienen significado y sirven para decidir
    System.out.println("\nINFORMACIÓN:");
    System.out.printf("  Temperatura promedio de la semana: %.2f °C%n", promedio);
    System.out.printf("  Día más caluroso: %s (%.1f °C)%n", dias[iMax], temp[iMax]);
    System.out.printf("  Día más frío    : %s (%.1f °C)%n", dias[iMin], temp[iMin]);
    System.out.println("  Días con más de 22 °C: " + calurosos);

    // 4. CONOCIMIENTO / DECISIÓN
    String decision = (promedio > 21) ? "aumentar el stock de helados"
                     : "mantener el stock normal";
    System.out.println("\nDECISIÓN para la heladería: " + decision);
  }
}
