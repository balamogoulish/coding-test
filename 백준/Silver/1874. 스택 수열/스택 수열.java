import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] targets = new int[n];
        for(int i=0; i<n; i++){
            targets[i] = sc.nextInt();
        }

        Stack<Integer> st = new Stack<>();
        int next = 1;
        StringBuilder sb = new StringBuilder();
        boolean success=true;

        for(int x: targets){
            while(next<=x) { //x가 올 때까지 push
                st.push(next++);
                sb.append("+\n");
            }
            //top이 x면 pop, 아니면 NO
            if(st.peek()==x){
                st.pop();
                sb.append("-\n");
            } else{
                success = false;
                break;
            }
        }
        if(success){
            System.out.println(sb.toString());
        }else{
            System.out.println("NO");
        }
    }
}
