import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer;
        Stack<Integer> cnt = new Stack<>();
        Stack<Integer> st = new Stack<>();
        
        for(int i=0; i<progresses.length; i++){
            int curr = (100-progresses[i])/speeds[i] + ((100-progresses[i])%speeds[i]==0 ? 0:1);
            if(!st.isEmpty() && st.peek()>=curr){ //앞에 소요날이 현재보다 크면 더하기
                int last = cnt.pop();
                cnt.push(last+1);
            }else{
                cnt.push(1);
                st.push(curr);
            }
        }
        
        answer = new int[cnt.size()];
        for(int i=0; i<cnt.size(); i++){
            answer[i] = cnt.get(i);
        }
        
        return answer;
    }
}