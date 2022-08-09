import java.io.InputStream;
import java.util.Scanner;

public class InputOutput {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // take string as input 
        String s = input.nextLine();
        System.out.println("You entered string - " + s);

        // take integer as input
        Integer i = input.nextInt();
        System.out.println("You entered string - " + i);

        float f = input.nextFloat();
        System.out.println("You entered float - " + f);
    }   
}
