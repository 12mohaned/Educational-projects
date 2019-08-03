import java.util.*;//allow you to take input from user
public class Nim {
    public static void main(String [] args) {
int marbles = (int)(Math.random()*90) +10;//number of marbles or gum
      System.out.println("Starting with " +marbles + " marbles");
      System.out.println("You play first.");
      Scanner sc = new Scanner(System.in);
      int user, computer;
      while(marbles != 1){//game end when number of marbles equals to one 
     System.out.println("Choose between 1 and " + marbles/2 + " marble(s)" );
        user = sc.nextInt();
        while(user<1 || user>marbles/2){/*marble is divided by 2 to give the
    user a chance to choose between certain range and to let computer have
    marbles left to choose from*/System.out.println("number of marbles available " + marbles);
     System.out.println("You entered a number outside the possible range! y  tizo l sayed");
     System.out.println("Choose between 1 and " + marbles/2 + " marble(s)" );
            user = sc.nextInt();
     }
     System.out.println("You chose "+ user + " marble(s)");
     marbles -= user;/*if we have 10 marbles and the user choose five then
     the no of marbles become 5 since we discard 5 chosen by user*/System.out.println(marbles + " marble(s) left.");
     if(marbles ==1){//whenever it reaches one when it's user turn he won 
     System.out.println("You win!!");
     break;
     }
     computer = (int)(Math.random()*(marbles/2)) +1;
     System.out.println("The computer chose " + computer + " marble(s)");
     marbles-= computer;
     System.out.println(marbles + " marble(s) left.");
     if(marbles ==1){
     System.out.println("You Lost!!");
     break;
     }
    }
  while(marbles >1);
    }
}