import java.util.*;

public class Main {

    static int[][] A;
    static int r_len = 3;
    static int c_len = 3;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        int k = sc.nextInt();
        A = new int[100][100];

        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                A[i][j] = sc.nextInt();
            }
        }

        int t = 0;
        while (t <= 100 && A[r-1][c-1] != k) {
            if (r_len >= c_len) { // R 연산
                sortRow();
            } else {              // C 연산
                sortCol();
            }
            t++;
        }

        if (t > 100) System.out.println(-1);
        else System.out.println(t);
    }

    // ---------------- R 연산 ----------------
    private static void sortRow() {
        int newC = 0;

        for (int r = 0; r < r_len; r++) {
            // 현재 행에서 논리적인 길이(c_len)만큼만 복사
            int[] row = new int[c_len];
            for (int c = 0; c < c_len; c++) {
                row[c] = A[r][c];
            }

            int[] x = sortArr(row, true); // 정렬된 결과(길이 100)

            // 결과를 A[r][*]에 반영
            for (int c = 0; c < 100; c++) {
                A[r][c] = x[c];
            }

            // 이 행의 실제 길이 갱신 (0 나오기 전까지)
            int len = 0;
            for (int c = 0; c < 100; c++) {
                if (x[c] == 0) break;
                len++;
            }
            newC = Math.max(newC, len);
        }

        c_len = newC;
    }

    // ---------------- C 연산 ----------------
    private static void sortCol() {
        int newR = 0;

        for (int c = 0; c < c_len; c++) {
            // 현재 열에서 논리적인 길이(r_len)만큼만 복사
            int[] col = new int[r_len];
            for (int r = 0; r < r_len; r++) {
                col[r] = A[r][c];
            }

            int[] x = sortArr(col, false); // 정렬된 결과(길이 100)

            // 결과를 A[*][c]에 반영
            for (int r = 0; r < 100; r++) {
                A[r][c] = x[r];
            }

            // 이 열의 실제 길이 갱신 (0 나오기 전까지)
            int len = 0;
            for (int r = 0; r < 100; r++) {
                if (x[r] == 0) break;
                len++;
            }
            newR = Math.max(newR, len);
        }

        r_len = newR;
    }

    // ---------------- 공통 정렬 로직 ----------------
    private static int[] sortArr(int[] arr, boolean isRow) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int x : arr) {
            if (x == 0) continue;
            hm.put(x, hm.getOrDefault(x, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(hm.entrySet());
        list.sort((e1, e2) -> {
            int comp = Integer.compare(e1.getValue(), e2.getValue()); // value 오름차순
            if (comp != 0) return comp;
            return Integer.compare(e1.getKey(), e2.getKey());         // key 오름차순
        });

        int[] result = new int[100];
        int i = 0;
        for (Map.Entry<Integer, Integer> e : list) {
            if (i >= 100) break;                  // 🔥 길이 100 제한
            result[i++] = e.getKey();
            if (i >= 100) break;                  // 🔥 value 넣다가 100 넘을 수도 있음
            result[i++] = e.getValue();
        }

        // isRow / isCol 에 따라 r_len / c_len 갱신은 여기서 안 하고,
        // 각각 sortRow / sortCol 에서 실제 길이 계산해서 갱신하도록 분리했음.
        return result;
    }
}
