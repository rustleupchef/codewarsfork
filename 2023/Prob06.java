/*
 * 
 * input is 3 nums
 * 
 * w h type (S for square or D for Diagonal)
 * 
 * 100 100 S
 * 300 100 D
 * 45 60 S 
 * 0 0 S       <-- End of input 
 */

import java.util.ArrayList;
import java.util.Scanner;

 public class Prob06{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList();
        String line, type;
        int w, h,p;
        // no prompt
        while(true){
            w = input.nextInt();
            h = input.nextInt();
            type = input.nextLine().strip();
            if(w == 0 && h == 0 && type.equals("S")){
                break;
            }
            else{
                if( type.equals("S")){
                    //  find perimter Plus extra for straight cut
                    p = 2*w + 2*h + 80;
                    //print result
                    System.out.println("Straight " + p);
                }
                else{
                    //  find perimter plus extra for diagonal cut
                    p = 2*w + 2*h + 8*40;
                    //print result
                    System.out.println("Diagonal " + p);
                }

            }
        }
    }
}
