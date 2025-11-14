import java.util.*;

public class Main {
    static int N;
    static int[] T;
    static int[] P;
    static int[] answer;
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        T = new int[N];
        P = new int[N];
        answer = new int[N+1];

        for(int i=0; i<N; i++) {
            T[i] = sc.nextInt();
            P[i] = sc.nextInt();
        }
        do_or_not(0, 0);
        Arrays.sort(answer);
        System.out.println(answer[N]);
    }

    private static void do_or_not(int idx, int price){
        answer[idx] = Math.max(answer[idx], price);

        if(idx+T[idx] == N) answer[N] = Math.max(answer[idx]+P[idx], answer[N]);
        // idx 날 상담을 하는 경우
        if(idx+T[idx] < N){
            do_or_not(idx+T[idx], answer[idx]+P[idx]);
        }
        // idx 날 상담을 하지 않는 경우
        if(idx+1 < N){
            do_or_not(idx+1, answer[idx]);
        }
    }
}
