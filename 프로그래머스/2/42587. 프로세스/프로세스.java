import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>(); // 인덱스 보관
        Queue<Integer> p = new LinkedList<>(); // 우선순위 보관

        for (int i = 0; i < priorities.length; i++) {
            q.add(i);
            p.add(priorities[i]);
        }

        while (!q.isEmpty()) {
            int idx = q.poll();
            int pri = p.poll();

            // 남은 항목 중 최대 우선순위를 확인 (p가 비었으면 바로 처리)
            if (!p.isEmpty() && Collections.max(p) > pri) {
                // 더 큰 우선순위가 뒤에 있으면 뒤로 보냄
                q.add(idx);
                p.add(pri);
            } else {
                // 현재 문서 출력
                answer++;
                if (idx == location) return answer;
            }
        }
        return answer;
    }
}
