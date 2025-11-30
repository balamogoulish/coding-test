

import java.util.*;

/**
 * 백준 14891 - 톱니바퀴
 * - 톱니 4개, 각 8칸
 * - 인덱스 기준:
 *   - 0 : 12시 방향
 *   - 2 : 오른쪽 맞닿는 톱니
 *   - 6 : 왼쪽 맞닿는 톱니
 */
public class Main {

    // wheels[톱니 번호][톱니 인덱스]
    static int[][] wheels = new int[4][8];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. 톱니 상태 입력
        for (int i = 0; i < 4; i++) {
            String line = sc.next(); // 예: "10101111"
            for (int j = 0; j < 8; j++) {
                wheels[i][j] = line.charAt(j) - '0';
            }
        }

        // 2. 회전 연산 개수
        int K = sc.nextInt();

        // 3. 회전 연산 처리
        for (int t = 0; t < K; t++) {
            int num = sc.nextInt() - 1; // 0-based 톱니 번호
            int dir = sc.nextInt();     // 1: 시계, -1: 반시계

            // 각 톱니가 이번 턴에 어느 방향으로 회전할지 저장
            int[] dirs = new int[4];
            dirs[num] = dir;

            // 왼쪽으로 전파
            for (int i = num - 1; i >= 0; i--) {
                // i와 i+1의 맞닿는 부분 비교
                // i     의 오른쪽: index 2
                // i + 1 의 왼쪽 : index 6
                if (wheels[i][2] != wheels[i + 1][6]) {
                    // 극이 다르면 반대 방향
                    dirs[i] = -dirs[i + 1];
                } else {
                    // 극이 같으면 그 왼쪽으로는 더 이상 전파 X
                    break;
                }
            }

            // 오른쪽으로 전파
            for (int i = num + 1; i < 4; i++) {
                // i-1 의 오른쪽: 2, i 의 왼쪽: 6
                if (wheels[i - 1][2] != wheels[i][6]) {
                    dirs[i] = -dirs[i - 1];
                } else {
                    break;
                }
            }

            // 실제 회전 적용
            for (int i = 0; i < 4; i++) {
                if (dirs[i] != 0) {
                    rotate(i, dirs[i]);
                }
            }
        }

        // 4. 점수 계산
        int score = 0;
        if (wheels[0][0] == 1) score += 1;  // 1번 톱니
        if (wheels[1][0] == 1) score += 2;  // 2번 톱니
        if (wheels[2][0] == 1) score += 4;  // 3번 톱니
        if (wheels[3][0] == 1) score += 8;  // 4번 톱니

        System.out.println(score);
    }

    /**
     * 톱니바퀴 회전
     *
     * @param id  : 회전할 톱니바퀴 인덱스 (0~3)
     * @param dir : 1 = 시계, -1 = 반시계
     */
    static void rotate(int id, int dir) {
        if (dir == 1) { // 시계 방향
            int last = wheels[id][7];
            for (int i = 7; i >= 1; i--) {
                wheels[id][i] = wheels[id][i - 1];
            }
            wheels[id][0] = last;
        } else if (dir == -1) { // 반시계 방향
            int first = wheels[id][0];
            for (int i = 0; i < 7; i++) {
                wheels[id][i] = wheels[id][i + 1];
            }
            wheels[id][7] = first;
        }
    }
}
