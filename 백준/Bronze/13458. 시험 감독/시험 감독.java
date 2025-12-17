import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for(int i=0; i<N; i++) A[i] = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        long answer = N;

        for(int a: A){
            int remain = a-B;
            if(remain>0){
                answer += (remain +C -1) /C;
            }
        }

        System.out.println(answer);
    }
}
