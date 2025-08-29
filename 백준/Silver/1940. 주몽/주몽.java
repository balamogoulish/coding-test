
import java.util.Arrays;
import java.util.Scanner;

/**
 * N 재료의 개수: 1~15,000
 * M 갑옷을 만드는데 필요한 수: 1~10,000,000(천만)
 * materials 재료 고유번호: 1~100,000 N개
 *
 * 1. materials를 정렬
 * 2. 투 포인터 방식 사용
 */
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] materials = new int[N];
        for (int i = 0; i < N; i++) materials[i] = sc.nextInt();
        Arrays.sort(materials);

        int start = 0, end = N - 1, count = 0;

        while (start < end) {                    // 교차 전까지만
            int sum = materials[start] + materials[end];
            if (sum == M) {                      // 한 쌍 발견
                count++;
                start++;
                end--;
            } else if (sum < M) {                // 더 키워야 함 → start++
                start++;
            } else {                             // 더 줄여야 함 → end--
                end--;
            }
        }
        System.out.println(count);
    }
}
