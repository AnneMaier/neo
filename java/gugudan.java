import java.util.*;

public class gugudan {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        do {
            System.out.println("Insert Number(0:exit) : ");
            int i = s.nextInt();

            if(i==0) {
                System.exit(1);
            } else if(i>1 && i<10) {
                for(int j=1; j<10; j++) {
                    System.out.println(i + " * " + j + "=" + i*j);
                }
            } else {
                System.out.println("Insert number between 2 ~ 9. Retype Again.");
            }
        } while(true);
    }
}