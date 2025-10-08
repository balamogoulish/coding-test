import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int time = 0; //현재 시간
        Queue<int[]> waitings = new LinkedList<>();

        // 소요시간 > 요청시간 > 작업번호 기준 오름차순
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            Comparator
                .comparingInt((int[] a) -> a[0])   // 소요시간
                .thenComparingInt(a -> a[1])       // 요청시간
                .thenComparingInt(a -> a[2])       // 작업 번호
        );

        for (int i = 0; i < jobs.length; i++) {
            // {소요시간, 요청시간, 작업번호}
            pq.offer(new int[]{ jobs[i][1], jobs[i][0], i });
        }
        
        while(!pq.isEmpty()){
            int[] curr = pq.poll();
            if(curr[1] > time){ //요청 시간이 현재 시간보다 크면 넘어가기
                waitings.add(curr);
            } else{
                time += curr[0];
                answer += time-curr[1];
                while(!waitings.isEmpty()){
                    pq.offer(waitings.remove());
                }
            }
            if(pq.isEmpty() && !waitings.isEmpty()){
                time++;
                while(!waitings.isEmpty()){
                    pq.offer(waitings.remove());
                }
            }
        }
        
        return answer/jobs.length;
    }
}
