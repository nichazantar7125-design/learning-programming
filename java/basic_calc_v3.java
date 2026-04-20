        import java.util.Scanner;

public class basic_calc_v3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double a;
        double b;
        int opcion;

        System.out.println("CALCULADORA");
        System.out.println("1 Sumar");
        System.out.println("2 Restar");
        System.out.println("3 Multiplicar");
        System.out.println("4 Dividir");
        System.out.println("5 Promedio");
        System.out.println("6 Todo");

        System.out.print("Elija una opcion: ");
        opcion = sc.nextInt();

        System.out.print("Numero 1: ");
        a = sc.nextDouble();

        System.out.print("Numero 2: ");
        b = sc.nextDouble();

        if (opcion == 1) {
            System.out.println("Resultado: " + (a + b));
        } else if (opcion == 2) {
            System.out.println("Resultado: " + (a - b));
        } else if (opcion == 3) {
            System.out.println("Resultado: " + (a * b));
        } else if (opcion == 4) {
            if (b != 0) {
                System.out.println("Resultado: " + (a / b));
            } else {
                System.out.println("No se puede dividir por 0");
            }
        } else if (opcion == 5) {
            System.out.println("Promedio: " + ((a + b) / 2));
        } else if (opcion == 6) {
            System.out.println("Suma: " + (a + b));
            System.out.println("Resta: " + (a - b));
            System.out.println("Multiplicacion: " + (a * b));
            if (b != 0) {
                System.out.println("Division: " + (a / b));
            } else {
                System.out.println("Division: no se puede");
            }
            System.out.println("Promedio: " + ((a + b) / 2));
        } else {
            System.out.println("Opcion incorrecta");
        }
        sc.close();
    }
}