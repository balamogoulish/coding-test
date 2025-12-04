import java.util.*;

public class Main {
    static int R;
    static int C;
    static int[][] room;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        R = sc.nextInt();
        C = sc.nextInt();
        int T = sc.nextInt();
        room = new int[R][C];

        int[] cleaner_up = new int[0];
        int[] cleaner_down = new int[0];
        for(int r=0; r<R; r++){
            for(int c=0; c<C; c++){
                int x = sc.nextInt();
                if(x==-1){
                    if(room[r-1][c]==-1){
                        cleaner_up = new int[]{r - 1, c};
                        cleaner_down = new int[]{r, c};
                    }
                }
                room[r][c] = x;
            }
        }
        for(int t=0; t<T; t++){
            extend_dust();
            operate_cleaner(cleaner_up, cleaner_down);
        }
        int answer = 2;
        for(int[] r: room){
            for(int rc: r){
                answer+=rc;
            };
        }
        System.out.println(answer);


    }

    // 미세먼지 확산
    private static void extend_dust(){
        int[][] room_updated = new int[R][C];
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        for(int r=0; r<R; r++){
            for(int c=0; c<C; c++){
                if(room[r][c] > 0){
                    int x = room[r][c]/5;
                    int cnt = 0;
                    for(int k=0; k<4; k++){
                        int nr = r+dr[k];
                        int nc = c+dc[k];
                        if(0<=nr && nr<R && 0<=nc && nc<C && room[nr][nc]!=-1){
                            room_updated[nr][nc]+= x;
                            cnt++;
                        }
                    }
                    room_updated[r][c]+=room[r][c]-x*cnt;
                }else if(room[r][c]==-1){
                    room_updated[r][c] = -1;
                }
            }
        }
        room = room_updated;
    }

    // 공기청정기 작동
    private static void operate_cleaner(int[] cleaner_up, int[] cleaner_down){
        int[][] room_updated = new int[R][C];

        int ur = cleaner_up[0];
        int uc = cleaner_up[1];
        int dr = cleaner_down[0];
        int dc = cleaner_down[1];

        for(int r=0; r<R; r++){
            for(int c=0; c<C; c++){
                if(room[r][c]<=0){
                    continue;
                }
                int nr = r;
                int nc = c;
                if(r==ur || r==dr){ //같은 행인 경우
                    if(c==C-1){
                        if(r==ur) nr--;
                        else nr++;
                    } else{
                        nc++;
                    }
                } else if(r==0 || r==R-1){ //가장 상단, 하단 행인 경우
                    if(c==0){
                        if(r==0) nr++;
                        else nr--;
                    } else nc--;
                } else if((c==0 && r<ur) || (c==C-1 && r>dr)) nr++;
                else if((c==0 && r>dr) || (c==C-1 && r<ur)) nr--;

                room_updated[nr][nc] = room[r][c];
            }
        }
        room_updated[ur][uc] = -1;
        room_updated[dr][dc] = -1;
        room = room_updated;
    }
}
