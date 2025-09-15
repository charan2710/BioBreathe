import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        
        System.out.print("enter your character :");
        char ch=sc.next().charAt(0);
         if((ch >='a' && ch <='z') || (ch>='A' && ch<='Z'))
         {
           System.out.println(ch +" : charcter is alphabet");
         }
         else {
           System.out.println(ch +": character is not a alphabet");
         }
}
}
