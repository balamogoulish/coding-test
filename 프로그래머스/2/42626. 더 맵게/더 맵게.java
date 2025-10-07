import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> hp = new PriorityQueue<>();
        for(int s: scoville){
            hp.offer(s);
        }
        
        while(hp.peek() < K){
            answer++;
            if(hp.size() < 2) return -1;
            int s1 = hp.poll();
            int s2 = hp.poll();
            int mixed = s1+(s2*2);
            hp.offer(mixed);
        }
        return answer;
    }
}