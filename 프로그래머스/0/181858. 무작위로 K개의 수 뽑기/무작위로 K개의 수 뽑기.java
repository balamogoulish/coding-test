import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        Arrays.fill(answer, -1);
        
        Set<Integer> seen = new HashSet<>();
        
        int idx=0;
        for(int num:arr){
            if(!seen.contains(num)){
                seen.add(num);
                answer[idx++] = num;
                if(idx==k) break;
            }
        }
        return answer;
    }
}