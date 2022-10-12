import java.util.*;
class num_guess
{
    public static void main()
    {
        Scanner in=new Scanner(System.in);
        System.out.println("Number Guess Game");
        double R=Math.random();
        double d=R*10+1;
        int r=(int)d;
        System.out.println("Enter a Number from 1 TO 10 ");
        int n=in.nextInt();
        int c=1;
        while(c>0)
        {
            if(n>r)
            {
                System.out.println(n+ " is Greater");
                System.out.println("The Number was "+r);
            }
            else
            {
                System.out.println(n+ " is Smaller");
                System.out.println("The Number was "+r);
            }
            System.out.println("Enter Another Number");
            n=in.nextInt();
            if(n==r)
            {
                if(c==1)
                {
                    System.out.println("*****/nCongratulations  ");
                }
                else if(c==2)
                {
                    System.out.println("***/nCongratulations  ");
                }
                else if(c==3)
                {
                    System.out.println("*/nCongratulations ");
                }
                else
                {
                    c=0;
                    System.out.println("You Win!");
                }
            }
        }

    }
}