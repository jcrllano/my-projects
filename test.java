import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.regex.Pattern;

public class test {
   
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);

      try {
        File myObj = new File("filename.txt");
        Scanner myReader = new Scanner(myObj);
        int i = 0;
        while (myReader.hasNextLine()) {
          if (i >= 1) {
            System.out.println("Enter Your Command:");  
          }
          else {
            System.out.println("Enter Your Greeting:");
          }
         // String input
         String word = sc.nextLine();
          String data = myReader.nextLine();
          // create a REGEX String
          String REGEX = "(.*)("+word+")(.*)?";
          boolean matcher = Pattern.matches(REGEX.toUpperCase(), data.toUpperCase());
          if (matcher) {
           i++;
           if (i >= 1) {
              REGEX = "(.*)(human response: "+word+")(.*)?";
              matcher = Pattern.matches(REGEX.toUpperCase(), data.toUpperCase());
              if (matcher) {
                System.out.println(data);
              }
           }
           else {
            System.out.println(data);
           }
          }
        }
        myReader.close();
      } catch (FileNotFoundException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
      }  
    }
}

