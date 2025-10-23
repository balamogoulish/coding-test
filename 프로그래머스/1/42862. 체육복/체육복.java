import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        // 1) 집합화 + 교집합(여벌도 있고 도난도 당한 경우) 제거
        Set<Integer> lostSet = IntStream.of(lost).boxed().collect(Collectors.toSet());
        Set<Integer> reserveSet = IntStream.of(reserve).boxed().collect(Collectors.toSet());
        // 교집합 처리: 자기 옷 입고 끝
        Set<Integer> both = new HashSet<>(lostSet);
        both.retainAll(reserveSet);
        lostSet.removeAll(both);
        reserveSet.removeAll(both);

        // 2) 각 학생이 가진 체육복 수 초기화: 기본 1
        int[] clothes = new int[n + 1]; // 1..n 사용
        Arrays.fill(clothes, 1);
        for (int i : lostSet)    clothes[i]--;
        for (int i : reserveSet) clothes[i]++;

        // 3) 빌려주기: i가 0이면 왼쪽(i-1) 우선, 안되면 오른쪽(i+1)
        for (int i = 1; i <= n; i++) {
            if (clothes[i] == 0) {
                if (i > 1 && clothes[i - 1] == 2) {
                    clothes[i - 1]--;
                    clothes[i]++;
                } else if (i < n && clothes[i + 1] == 2) {
                    clothes[i + 1]--;
                    clothes[i]++;
                }
            }
        }

        // 4) 체육수업 가능한 학생 수
        int answer = 0;
        for (int i = 1; i <= n; i++) if (clothes[i] > 0) answer++;
        return answer;
    }
}
