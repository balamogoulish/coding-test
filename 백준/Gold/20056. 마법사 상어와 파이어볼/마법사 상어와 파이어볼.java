
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {

    static class Fireball {
        int r, c; // 0-based 행, 열
        int m;    // 질량
        int s;    // 속력
        int d;    // 방향

        Fireball(int r, int c, int m, int s, int d) {
            this.r = r;
            this.c = c;
            this.m = m;
            this.s = s;
            this.d = d;
        }
    }

    static int N, M, K;
    // 8방향: 0부터 7까지
    // 0: 위, 1: 우상, 2: 오른쪽, 3: 우하, 4: 아래, 5: 좌하, 6: 왼쪽, 7: 좌상
    static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};

    static List<Fireball> fireballs = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1; // 0-based
            int c = Integer.parseInt(st.nextToken()) - 1; // 0-based
            int m = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            fireballs.add(new Fireball(r, c, m, s, d));
        }

        for (int t = 0; t < K; t++) {
            if (fireballs.isEmpty()) break; // 다 사라졌으면 더 볼 필요 없음
            moveAll();
            mergeAndSplit();
        }

        int answer = 0;
        for (Fireball fb : fireballs) {
            answer += fb.m;
        }
        System.out.println(answer);
    }

    // 1. 모든 파이어볼 이동
    private static void moveAll() {
        // 각 칸에 있는 파이어볼 리스트 저장용
        @SuppressWarnings("unchecked")
        List<Fireball>[][] board = new ArrayList[N][N];

        for (Fireball fb : fireballs) {
            // 속력은 N으로 나눈 나머지만큼만 실제로 의미 있음 (원형 격자)
            int move = fb.s % N;

            int nr = (fb.r + dr[fb.d] * move) % N;
            int nc = (fb.c + dc[fb.d] * move) % N;

            if (nr < 0) nr += N;
            if (nc < 0) nc += N;

            if (board[nr][nc] == null) {
                board[nr][nc] = new ArrayList<>();
            }
            board[nr][nc].add(new Fireball(nr, nc, fb.m, fb.s, fb.d));
        }

        // 이동 결과만 다시 fireballs에 담음 (합치기/나누기는 다음 단계에서)
        fireballs.clear();
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (board[r][c] != null) {
                    fireballs.addAll(board[r][c]);
                }
            }
        }
    }

    // 2. 같은 칸에 2개 이상이면 합치고 나누기
    private static void mergeAndSplit() {
        // 칸별로 다시 모은 뒤 처리
        @SuppressWarnings("unchecked")
        List<Fireball>[][] board = new ArrayList[N][N];

        for (Fireball fb : fireballs) {
            if (board[fb.r][fb.c] == null) {
                board[fb.r][fb.c] = new ArrayList<>();
            }
            board[fb.r][fb.c].add(fb);
        }

        List<Fireball> newList = new ArrayList<>();

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (board[r][c] == null) continue;

                List<Fireball> cell = board[r][c];
                int size = cell.size();

                // 파이어볼이 1개면 그대로 유지
                if (size == 1) {
                    newList.add(cell.get(0));
                    continue;
                }

                // 2개 이상이면 합쳐서 나누기
                int sumM = 0;
                int sumS = 0;
                boolean allEven = true;
                boolean allOdd = true;

                for (Fireball fb : cell) {
                    sumM += fb.m;
                    sumS += fb.s;
                    if (fb.d % 2 == 0) {
                        allOdd = false;
                    } else {
                        allEven = false;
                    }
                }

                int newM = sumM / 5;
                if (newM == 0) {
                    // 질량 0이면 이 칸에선 아무것도 안 남음
                    continue;
                }

                int newS = sumS / size;
                int[] dirs;
                if (allEven || allOdd) {
                    dirs = new int[]{0, 2, 4, 6};
                } else {
                    dirs = new int[]{1, 3, 5, 7};
                }

                for (int d : dirs) {
                    newList.add(new Fireball(r, c, newM, newS, d));
                }
            }
        }

        fireballs = newList;
    }
}
