import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[][] baskets;
    static boolean[][] clouds;

    static int[] dr = {0, -1, -1, -1, 0, 1, 1, 1};
    static int[] dc = {-1, -1, 0, 1, 1, 1, 0, -1};

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        baskets = new int[N][N];
        int[][] moves = new int[M][2];
        clouds = new boolean[N][N];
        for(int r=0; r<N; r++){
            for(int c=0; c<N; c++){
                baskets[r][c] = sc.nextInt();
            }
        }
        for(int m=0; m<M; m++){
            moves[m][0] = sc.nextInt()-1;
            moves[m][1] = sc.nextInt();
        }
        clouds[N-2][0] = true;
        clouds[N-2][1] = true;
        clouds[N-1][0] = true;
        clouds[N-1][1] = true;

        for(int[] move: moves){
            //1. 모든 구름을 d방향으로 s칸 이동 + 1씩 물의 양 증가
            List<int[]> moved_clouds = move_clouds_and_rain(move[0], move[1]);
            //2. 1에서 물이 증가한 칸에 물복사 버그 마법 시전
            for(int[] cloud: moved_clouds){
                baskets[cloud[0]][cloud[1]]+=get_cnt_near_water(cloud[0], cloud[1]);
            }
            //3. 바구니에 저장된 물의 양이 2이상인 모든 칸(1에서 이동된 구름은 사라짐)에 구름이 생기고 물의 양이 2 감소
            boolean[][] tmp = new boolean[N][N];
            for(int r=0; r<N; r++){
                for(int c=0; c<N; c++){
                    if(!clouds[r][c] && baskets[r][c]>=2){
                        baskets[r][c]-=2;
                        tmp[r][c] = true;
                    }
                }
            }
            clouds = tmp;
        }
        int answer = 0;
        for(int[] basket: baskets){
            for(int b: basket) answer+=b;
        }
        System.out.println(answer);
    }

    static List<int[]> move_clouds_and_rain(int d, int s){
        List<int[]> moved_clouds = new ArrayList<>();
        boolean[][] tmp = new boolean[N][N];
        for(int r=0; r<N; r++){
            for(int c=0; c<N; c++){
                if(clouds[r][c]){ //구름이 있는 경우 이동
                    int nr = get_nxt(r, dr[d]*s);
                    int nc = get_nxt(c, dc[d]*s);
                    int[] n_cloud = {nr, nc};
                    moved_clouds.add(n_cloud);
                    baskets[nr][nc]++;
                    tmp[nr][nc] = true;
                }
            }
        }
        clouds = tmp;
        return moved_clouds;
    }

    static int get_cnt_near_water(int r, int c){
        int[] diagonal_r = {1, 1, -1, -1};
        int[] diagonal_c = {1, -1, 1, -1};
        int waters = 0;
        for(int k=0; k<4; k++){
            int nr = r+diagonal_r[k];
            int nc = c+diagonal_c[k];
            if(0<=nr && nr<N && 0<=nc && nc<N && baskets[nr][nc]>0) waters++;
        }
        return waters;
    }

    static int get_nxt(int curr, int move){
        return (((curr+move+N)%N)+N)%N;
    }
}

