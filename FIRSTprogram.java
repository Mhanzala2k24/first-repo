import java.util.Scanner;

public class FIRSTprogram {


public static void main(String[] args) {
    Sum();
    // for (int i = 0; i <=20; i++ ){
    //     System.out.println("PAKISTAN  ZINDABAD");
    // }
    // for (int b = 0; b<11; b+=2){
    //     System.out.println(b);
    // }

    // int c = 0;
    // while(c <= 10){
    //     System.out.println(c);
    //     c++;
    // }

    // int d = 0;
    // do{
    //     System.out.println(d);
    //     d+= 10;
    // }while(d <=1000);

 //  int a = 12;
    // while (a < 11){
    //     System.out.println("PAKISTAN ZINDABAD!");
    //     a++;
    // }

    //  do{
    //      System.out.println("PAKISTAN ZINDABAD");
    //      a += 2;
    //  }while (a <=11);
    }
     public static void Sum(){
        Scanner input = new Scanner (System.in);
        System.out.println("ENTER THE NUMBER: ");
        int f = input.nextInt();

        int i = 0;
        while(i <= f){
            System.out.println(i);
            i += 2;
        }

     }

}