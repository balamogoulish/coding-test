/**
 * 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
 * 2. 1을 만족하는 칸이 여러 개면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸을 선택한다.
 * 3. 2를 만족하는 칸이 여러 개면, 행의 번호가 작은 칸, 열의 번호가 작은 칸으로 정한다.
 *
 */

import java.util.*;
public class Main {
    static int N;
    static int[][] seats; //자리 배치
    static HashMap<Integer, List<Integer>> friends; //friends[i]: [i가 좋아하는 학생 배열]

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        seats = new int[N][N];
        friends = new HashMap<>();

        //학생 순회하면서 자리 찾기
        for(int i=0; i<N*N; i++){
            int me = sc.nextInt();
            List<Integer> fs = new ArrayList<>();
            for(int j=0; j<4; j++){
                fs.add(sc.nextInt());
            }
            friends.put(me, fs);

            int[] seat = with_many_friends_seats(me, fs);
            seats[seat[0]][seat[1]] = me;
        }

        int answer = 0;
        for(int r=0; r<N; r++){
            for(int c=0; c<N; c++){
                answer+=get_score(r, c, friends.get(seats[r][c]));
            }
        }

        System.out.println(answer);
    }

    /**
     *
     * @param me: 자리를 찾을 me
     * @param my_friends: me가 좋아하는 friends 목록
     */
    private static int[] with_many_friends_seats(int me, List<Integer> my_friends){
        int max_friends = -1; //인근 최대 친구 수
        int max_emptys = -1; //인근 최대 빈칸 수
        int[] rc = {0, 0};
        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};

        for(int r=0; r<N; r++){
            for(int c=0; c<N; c++){
                if(seats[r][c]==0){ //비어있는 칸인지 여부
                    int fs = 0;
                    int es = 0;
                    //인근 칸 탐색
                    for(int k=0; k<4; k++){
                        int nr = r+dr[k];
                        int nc = c+dc[k];
                        if(0<=nr && nr<N && 0<=nc && nc<N){
                            if(seats[nr][nc]==0) es++; //비어있는 경우
                            if(my_friends.contains(seats[nr][nc])) fs++; //좋아하는 친구가 있는 경우
                        }
                    }
                    if(max_friends < fs || (max_friends == fs && max_emptys < es)){
                        max_friends = fs;
                        max_emptys = es;
                        rc[0] = r;
                        rc[1] = c;
                    }
                }
            }
        }

        return rc;
    }

    private static int get_score(int r, int c, List<Integer> my_friends){
        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};
        int fs = 0;
        for(int k=0; k<4; k++){
            int nr = r+dr[k];
            int nc = c+dc[k];
            if(0<=nr && nr<N && 0<=nc && nc<N){
                if(my_friends.contains(seats[nr][nc])) fs++; //좋아하는 친구가 있는 경우
            }
        }
        return fs==0 ? 0 : (int) Math.pow(10, fs - 1);
    }
}
