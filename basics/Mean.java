import java.util.*;

public class Mean {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int sum = 0, count = 0;
        // loop runs until the user input is of type integer
        while(input.hasNextInt()) {
            int num = input.nextInt();
            sum += num;
            count += 1;
        }

        int mean = sum / count ;
        System.out.println("Mean of given number - " + mean);
    }
}
