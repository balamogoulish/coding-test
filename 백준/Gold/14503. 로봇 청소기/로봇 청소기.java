import java.util.*;

/**
 * 0: 북쪽
 * 1: 동쪽
 * 2: 남쪽
 * 3: 서쪽
 */
public class Main {
    static int N;
    static int M;
    static int[][] room;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        int r = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();

        room = new int[N][M];
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++) room[i][j] = sc.nextInt();
        }
        int answer = get_clean_space(r, c, d);
        System.out.println(answer);
    }

    //시작점 sr, sc 에서 방향 sd일 때, 청소한 칸의 수 반환
    private static int get_clean_space(int sr, int sc, int sd){
        int x = 0;
        while(true){
            //1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
            if(room[sr][sc]==0){
                room[sr][sc] = 2;
                x++;
            }
            //2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            int nxt_d = get_nxt_direction(sr, sc, sd);
            if(nxt_d == -1){
                int nr = sr-dr[sd];
                int nc = sc-dc[sd];
                //2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                if(0<=nr && nr<N && 0<=nc && nc<M && room[nr][nc] != 1){
                    sr = nr;
                    sc = nc;
                    continue;
                } else { //바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                    break;
                }
            } else{
                sd = nxt_d;
                sr = sr+dr[sd];
                sc = sc+dc[sd];
            }
        }
        return x;
    }

    //현재 칸의 주변 4칸 중 청소되지 않은 칸이 있는 경우 판별
    //왼쪽으로 90도 회전하면서 판별 후, 있으면 해당 방향 반환, 없으면 -1 반환
    private static int get_nxt_direction(int r, int c, int d){
        for(int i=0; i<4; i++){
            d = get_change_direction(d);
            int nr = r+dr[d];
            int nc = c+dc[d];
            if(0<=nr && nr<N && 0<=nc && nc<M && room[nr][nc] == 0) {
                return d;
            }
        }
        return -1;
    }

    //현재 방향에서 반시계 방향으로 돌린 방향 반환
    private static int get_change_direction(int d){
        return (d+3)%4;
    }
}
