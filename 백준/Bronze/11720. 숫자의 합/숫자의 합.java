import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        int sum = 0;

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String sNums = sc.next();
        char[] cNums = sNums.toCharArray();

        for(int i=0; i<N; i++){
//            answer+=Integer.parseInt(cNums[i]+"");
            sum+=cNums[i]-'0';
        }
        System.out.println(sum);
    }

}