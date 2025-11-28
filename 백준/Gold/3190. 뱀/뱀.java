import java.util.*;

/**
 * 시작 위치(0,0)
 * 큐를 사용
 * - 머리를 다음칸으로 이동 -> offerFirst();
 * - 사과가 없는 경우 -> poll();
 */

public class Main {
    static int N;
    static int K;
    static int L;
    static boolean[][] apples;
    static int[] directions;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();
        apples = new boolean[N][N]; //사과 좌표 배열
        for(int i=0; i<K; i++){
            int r = sc.nextInt();
            int c = sc.nextInt();
            apples[r-1][c-1] = true;
        }
        L = sc.nextInt();
        directions = new int[10001];
        for(int i=0; i<L; i++){
            int t = sc.nextInt();
            String d = sc.next();
            if(d.equals("D")){
                directions[t] = 1;
            } else{
                directions[t] = -1;
            }
        }

      System.out.println(get_play_time());
    }

    //게임 시간 구하기
    private static int get_play_time(){
        int t = 0;
        boolean[][] board = new boolean[N][N];
        Deque<int[]> snake = new LinkedList<>();
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};

        board[0][0] = true; //시작 위치 false
        int[] tmp = {0, 0};
        snake.add(tmp); //뱀이 차지하는 칸
        int dir_id = 0; //초기 방향

        while(true){
            //1. 현재 방향 전환 여부 확인
            if(directions[t]!=0){
                dir_id = get_dir_id(dir_id, directions[t]);
            }
            t++;
            int[] curr = snake.peekFirst();
            int nr = curr[0]+dr[dir_id];
            int nc = curr[1]+dc[dir_id];

            //2. 뱀이 다음 칸으로 이동할 수 있는 지 판별
            if(is_able_to_move(nr, nc, board)){
                //뱀 머리 추가 & board도 처리
                int[] nxt = {nr, nc};
                snake.offerFirst(nxt);
                board[nr][nc] = true;
                if(!apples[nr][nc]) { //사과가 없는 경우
                    int[] tail = snake.pollLast();
                    board[tail[0]][tail[1]] = false;
                } else{
                    apples[nr][nc] = false;
                }
            }else{
                break;
            }
        }

        return t;
    }

    //방향 전환 시 방향 인덱스 반환
    private static int get_dir_id(int id, int d){
        if(d==1){ //오른쪽 전환 시
            return (id+1)%4;
        } else{
            return (id+3)%4;
        }
    }

    //다음 칸으로 이동 가능 여부
    private static boolean is_able_to_move(int r, int c, boolean[][] board){
        if(0<=r && r<N && 0<=c && c<N){//1. 해당 칸이 보드 내인지
            if(!board[r][c]){//2. 해당 칸을 뱀이 차지하고 있지 않은지
                return true;
            }
        }
        return false;
    }
}