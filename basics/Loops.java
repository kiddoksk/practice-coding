public class Loops {
    public static void main(String[] args) {
        for (int i = 1; i < 10; i ++) {
            if (i < 8)
                System.out.println(i);
        }
        int i = 1;
        while (i <= 5) {
            System.out.println("I is less that 5 - " + i);
            i +=1;
        }
    }
}

/*
    output 
    1
    2
    3
    4
    5
    6
    7
    I is less that 5 - 1
    I is less that 5 - 2
    I is less that 5 - 3
    I is less that 5 - 4
    I is less that 5 - 5
 */