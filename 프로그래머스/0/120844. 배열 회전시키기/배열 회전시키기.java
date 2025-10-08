import java.util.*;

class Solution {
    public int[] solution(int[] numbers, String direction) {
        int[] answer = new int[numbers.length];
        Deque<Integer> dq = new LinkedList<>();
        for(int num : numbers){
            dq.offerLast(num);
        }
        
        if(direction.equals("left")){
            int x = dq.pollFirst();
            dq.offerLast(x);
        } else{
            int x = dq.pollLast();
            dq.offerFirst(x);
        }
        
        for(int i=0; i<numbers.length; i++){
            answer[i] = dq.pollFirst();
        }
        return answer;
    }
}