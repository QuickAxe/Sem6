import java.util.Scanner;

public class cal {
    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);

        System.out.println("Enter the two mnumbers: ");
        float a = scn.nextFloat();
        float b = scn.nextFloat();

        System.out.println("Enter :\n1.To add\n2.To subtract\n3.To multiply\n4.To divide\nOption: ");

        int choice = scn.nextInt();

        switch (choice) {
            case 1:
                System.out.println("Answer = " + (a + b));
                break;
            case 2:
                System.out.print("Answer= " + (a - b));
                break;
            case 3:
                System.out.println("answer= " + (a * b));
                break;
            case 4:
                System.out.println("NAswer=" + (a / b));
            default:
                System.out.println("wrong choice\n\n");
        }

        System.out.println("\n\n");
    }
}