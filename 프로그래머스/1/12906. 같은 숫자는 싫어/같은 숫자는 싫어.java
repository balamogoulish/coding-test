import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        int[] answer;
        Stack<Integer> st = new Stack<>();
        
        for(int n: arr){
            if(!st.isEmpty() && st.peek()==n){
                continue;
            }
            st.push(n);
        }
        
        answer = new int[st.size()];
        for(int i=0; i<st.size(); i++){
            answer[i] = st.get(i);
        }
        return answer;
    }
}