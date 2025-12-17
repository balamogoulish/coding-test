import java.util.*;

/**
 * L개의 연속된 칸에 경사로의 바닥이 모두 접해야 함
 * 높은 칸과 낮은 칸의 차이는 1이어야 한다.
 * 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어야 한다.
 */
public class Main {
    static int N;
    static int L;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        L = sc.nextInt();
        int[][] board = new int[N][N];
        for(int r=0; r<N; r++) for(int c=0; c<N; c++) board[r][c] = sc.nextInt();

        int answer = get_load_cnt(board);
        System.out.println(answer);
    }

    static private int get_load_cnt(int[][] board){
        int cnt = 0;
        for(int i=0; i<N; i++){
            int[] row = new int[N];
            int[] col = new int[N];
            for(int j=0; j<N; j++){
                row[j] = board[i][j];
                col[j] = board[j][i];
            }
            if(is_available(row)) cnt++;
            if(is_available(col)) cnt++;
        }
        return cnt;
    }

    static private boolean is_available(int[] load){
        boolean[] is_ramp = new boolean[N];

        for(int i=1; i<N; i++){

            if(load[i-1] > load[i]){            //이전 칸이 높은 경우
                for(int nxt=0; nxt<L; nxt++){
                    if(i+nxt>=N || load[i+nxt]+1 != load[i-1] || is_ramp[i+nxt]) return false;
                    is_ramp[i+nxt] = true;
                }
            } else if(load[i-1] < load[i]){            //다음 칸이 높은 경우
                for(int nxt=1; nxt<=L; nxt++){
                    if(i-nxt<0 || load[i-nxt]+1 != load[i] || is_ramp[i-nxt]) return false;
                    is_ramp[i-nxt] = true;
                }
            }
        }
        return true;
    }
}
