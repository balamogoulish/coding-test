import java.util.*;

public class Main {
    static int N;
    static int[] A;
    static int[] op_cnt = new int[4];
    static int MAX = -1000000001;
    static int MIN = 1000000001;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        A = new int[N];
        for(int i=0; i<N; i++) A[i] = sc.nextInt();
        for(int i=0; i<4; i++) op_cnt[i] = sc.nextInt();

        dfs(A[0],1);

        System.out.println(MAX);
        System.out.println(MIN);
    }

    static void dfs(int num, int idx){
        if(idx==N){
            MAX = Math.max(MAX, num);
            MIN = Math.min(MIN, num);
            return;
        }
        for(int i=0; i<4; i++){
            if(op_cnt[i] > 0){
                op_cnt[i]--;

                switch(i){
                    case 0: dfs(num+A[idx], idx+1); break;
                    case 1: dfs(num-A[idx], idx+1); break;
                    case 2: dfs(num*A[idx], idx+1); break;
                    case 3: dfs(num/A[idx], idx+1); break;
                }
                op_cnt[i]++;
            }
        }
    }
}
