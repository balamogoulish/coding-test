
import java.io.*;
import java.util.*;

/**
 * 6: 벽
 * 1~5: CCTV
 */
public class Main {
    static int N, M;
    static int[][] room;
    static List<CCTV> cctvs = new ArrayList<>();
    static int ans = Integer.MAX_VALUE;

    // 0:상, 1:우, 2:하, 3:좌
    static final int[] dr = {-1, 0, 1, 0};
    static final int[] dc = {0, 1, 0, -1};

    // CCTV 타입별 가능한 방향 조합
    static final int[][][] DIRS = {
            {}, // 0 dummy
            {{0}, {1}, {2}, {3}},                 // 1
            {{0, 2}, {1, 3}},                     // 2
            {{0, 1}, {1, 2}, {2, 3}, {3, 0}},     // 3
            {{0, 1, 2}, {1, 2, 3}, {2, 3, 0}, {3, 0, 1}}, // 4
            {{0, 1, 2, 3}}                        // 5
    };

    static class CCTV {
        int r, c, type;
        CCTV(int r, int c, int type) {
            this.r = r; this.c = c; this.type = type;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        room = new int[N][M];

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < M; c++) {
                room[r][c] = Integer.parseInt(st.nextToken());
                if (1 <= room[r][c] && room[r][c] <= 5) {
                    cctvs.add(new CCTV(r, c, room[r][c]));
                }
            }
        }

        dfs(0, room);
        System.out.println(ans);
    }

    static void dfs(int idx, int[][] board) {
        if (idx == cctvs.size()) {
            ans = Math.min(ans, countZero(board));
            return;
        }

        CCTV cam = cctvs.get(idx);
        int[][] options = DIRS[cam.type];

        for (int[] dirs : options) {
            int[][] next = copy(board);
            for (int d : dirs) watch(next, cam.r, cam.c, d);
            dfs(idx + 1, next);
        }
    }

    static void watch(int[][] board, int r, int c, int dir) {
        int nr = r + dr[dir];
        int nc = c + dc[dir];

        while (0 <= nr && nr < N && 0 <= nc && nc < M) {
            if (board[nr][nc] == 6) break;      // 벽이면 종료
            if (board[nr][nc] == 0) board[nr][nc] = -1; // 빈칸만 감시 표시
            // CCTV(1~5)나 이미 감시(-1)는 그냥 통과
            nr += dr[dir];
            nc += dc[dir];
        }
    }

    static int countZero(int[][] board) {
        int cnt = 0;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (board[r][c] == 0) cnt++;
            }
        }
        return cnt;
    }

    static int[][] copy(int[][] src) {
        int[][] dst = new int[N][M];
        for (int i = 0; i < N; i++) dst[i] = src[i].clone();
        return dst;
    }
}