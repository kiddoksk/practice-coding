public class MaxOfThreeNumbers {
    public static void main(String [] args) {
        int a = 10, b = 20, c = 1;
        int result;

        result = ((a > b) ? (a > c) ? a : c : (b > c) ? b : c);
        System.out.println("Maximum number is - " + result);
    }
}