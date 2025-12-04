import java.util.*;

public class Main {
    static int answer = 0;
    static int N;
    static int M;
    static int[][] board;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        board = new int[N][M];
        for(int r=0; r<N; r++){
            for(int c=0; c<M; c++){
                board[r][c] = sc.nextInt();
            }
        }

        boolean[][] visited = new boolean[N][M];
        for(int r=0; r<N; r++){
            for(int c=0; c<M; c++){
                List<int[]> tetrominos = new ArrayList<>();
                int[] curr = {r, c};
                tetrominos.add(curr);
                visited[r][c] = true;
                dfs(tetrominos, visited, 1, board[r][c]);
            }
        }
        System.out.println(answer);

    }

    /**
     *
     * @param tetrominos: 테트로미노가 놓인 칸
     * @param cnt: 테트로미노가 놓인 칸 수
     * @param sum: 테트로미노가 톻인 칸에 쓰인 수의 합
     */
    private static void dfs(List<int[]> tetrominos, boolean[][] visited, int cnt, int sum){
        if(cnt==4){
            answer = Math.max(answer, sum);
            return;
        }

        int[] dr = {0, 0, -1, 1};
        int[] dc = {-1, 1, 0, 0};

        for(int i = 0; i<cnt; i++){
            int[] curr = tetrominos.get(i);
            for(int k=0; k<4; k++){
                int nr = dr[k]+curr[0];
                int nc = dc[k]+curr[1];
                if(0<=nr && nr<N && 0<=nc && nc<M && !visited[nr][nc]){
                    visited[nr][nc] = true;
                    int[] nxt = {nr, nc};
                    tetrominos.add(nxt);
                    dfs(tetrominos, visited, cnt+1, sum+board[nr][nc]);
                    visited[nr][nc] = false;
                    tetrominos.remove(tetrominos.size()-1);
                }
            }
        }

    }
}
