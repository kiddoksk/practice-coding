import java.util.*;
public class IfElse {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter value of A");
        Integer a = sc.nextInt();
        
        System.out.println("Enter value of B");
        Integer b = sc.nextInt();

        System.out.println("Enter value of C");
        Integer c = sc.nextInt();

        if ( a > b && a > c)
            System.out.println("A is greater than B and C");
        else if ( b > a && b > c)
            System.out.println("B is greater than A and B");
        else
            System.out.println("C is greater");
    }
}

/*
Output - 
Enter value of A
1
Enter value of B
6
Enter value of C
2
B is greater than A and B
 */ 