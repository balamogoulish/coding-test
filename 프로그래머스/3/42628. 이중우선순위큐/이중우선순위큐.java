import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {0, 0};
        int count = 0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((o1, o2)->o2-o1);
        for(String op: operations){
            if(op.equals("D -1")){ //큐에서 최솟값 삭제
                if(count<1) continue;
                maxHeap.remove(minHeap.poll());
                count--;
            } else if(op.equals("D 1")){ //큐에서 최댓값 삭제
                if(count<1) continue;
                minHeap.remove(maxHeap.poll());
                count--;
            } else{ //큐에 삽입
                String[] num = op.split(" ");
                minHeap.offer(Integer.parseInt(num[1]));
                maxHeap.offer(Integer.parseInt(num[1]));
                count++;
            }
        }
        
        answer[1] =minHeap.isEmpty() ? 0 : minHeap.poll();
        answer[0] =maxHeap.isEmpty() ? 0 : maxHeap.poll();
        return answer;
    }
}