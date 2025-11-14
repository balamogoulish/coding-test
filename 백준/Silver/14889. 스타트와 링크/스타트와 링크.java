import java.util.*;

public class Main {
    static int N;
    static int[][] S;
    static boolean[] selected;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        S = new int[N][N];

        for(int r=0; r<N; r++){
            for(int c=0; c<N; c++){
                S[r][c] = sc.nextInt();
            }
        }
        selected = new boolean[N];
        dfs(0, 0);
        System.out.println(answer);
    }

    static void dfs(int idx, int cnt){
        if(cnt==N/2){
            calc();
            return;
        }

        if(idx>=N) return;

        for(int i=idx; i<N; i++){
            selected[i] = true;
            dfs(i+1, cnt+1);
            selected[i] = false;
        }
    }

    static void calc(){
        int start = 0;
        int link = 0;

        for(int i=0; i<N; i++){
            for(int j=i+1; j<N; j++){
                int tmp = S[i][j]+S[j][i];
                if(selected[i] && selected[j]) start+=tmp;
                else if(!selected[i] && !selected[j]) link+=tmp;
            }
        }
        answer = Math.min(answer, Math.abs(start-link));
        if(answer==0){
            System.out.println(answer);
            System.exit(0);
        }
    }
}
