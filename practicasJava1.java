import java.util.Scanner;

public class practicasJava1 {
    public static void main(String[] args) {

        //Switch
        Scanner diaDeLaSemana = new Scanner(System.in);

        System.out.println("Escribe un dia de la semana: ");
        String dia = diaDeLaSemana.nextLine();
        System.out.println("Has elegido " + dia);

        switch (dia) {
            case "Lunes" -> System.out.println(dia + " Es un dia laboral. :(");
            case "Martes" -> System.out.println(dia + " Es un dia laboral. :(");
            case "Miercoles" -> System.out.println(dia + " Es un dia laboral. :(");
            case "Jueves" -> System.out.println(dia + " Es un dia laboral. :(");
            case "Viernes" -> System.out.println(dia + " Es un dia laboral. :(");
            case "Sabado" -> System.out.println(dia + " No es un dia laboral. :)");
            case "Domingo" -> System.out.println(dia + " No es un dia laboral. :)");
            default -> System.out.println("No has elegido un dia");
        }

        //Ventas
        Scanner ventas = new Scanner(System.in);

        System.out.println("Numero de manzanas vendidas: ");
        int manzanas = ventas.nextInt();
        System.out.println("Numero de peras vendidas: ");
        int peras = ventas.nextInt();
        System.out.println("Numero de aguacates vendidos: ");
        int aguacates = ventas.nextInt();
        System.out.println("Numero de melones vendidos: ");
        int melones = ventas.nextInt();

        System.out.println("Vendiste " + manzanas + " manzana(s).");
        System.out.println("Vendiste " + peras + " pera(s).");
        System.out.println("Vendiste " + aguacates + " aguacate(s).");
        System.out.println("Vendiste " + melones + " melon(s).");

        Scanner precio = new Scanner(System.in);

        System.out.println("Precio de unidad manzana: ");
        double precioManzana = precio.nextDouble();
        System.out.println("Precio de unidad pera: ");
        double precioPera = precio.nextDouble();
        System.out.println("Precio de unidad aguacate: ");
        double precioAguacate = precio.nextDouble();
        System.out.println("Precio de unidad melon: ");
        double precioMelon = precio.nextDouble();

        System.out.println("La unidad de manzana vale: " + precioManzana);
        System.out.println("La unidad de pera vale: " + precioPera);
        System.out.println("La unidad de aguacate vale: " + precioAguacate);
        System.out.println("La unidad de melon vale: " + precioMelon);

        double gananciasManzana = (manzanas * precioManzana);
        double gananciasPera = (peras * precioPera);
        double gananciasAguacate = (aguacates * precioAguacate);
        double gananciasMelon = (melones * precioMelon);

        System.out.println("Hiciste $ " + gananciasManzana + " en manzanas");
        System.out.println("Hiciste $ " + gananciasPera + " en peras");
        System.out.println("Hiciste $ " + gananciasAguacate + " en aguacates");
        System.out.println("Hiciste $ " + gananciasMelon + " en melones");

        System.out.println("Las ganancias totales son de: $ " + (gananciasManzana + gananciasPera + gananciasAguacate + gananciasMelon));
        
        //Do while
        int numeroDigitado = 0;

        do {
            Scanner numero = new Scanner(System.in);

            System.out.println("Digite un numero igual o mayor que 0: ");
            numeroDigitado = numero.nextInt();

            if (numeroDigitado > 0) {
                System.out.println("Digitaste el numero " + numeroDigitado + ": Este numero es mayor que 0");
            } else if (numeroDigitado == 0) {
                System.out.println("Digitaste el numero " + numeroDigitado + ": Este numero es igual a 0");
            } else {
                System.out.println("Elegiste el numero " + numeroDigitado + ": Este numero es menor que 0");
            }
        } while (numeroDigitado < 0) ;

        System.out.println("Saliste del bucle al digitar un numero igual o mayor que 0");
    }
}