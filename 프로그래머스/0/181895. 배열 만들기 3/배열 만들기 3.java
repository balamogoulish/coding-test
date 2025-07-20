import java.util.*;

class Solution {
    public List solution(int[] arr, int[][] intervals) {
        List<Integer> answer = new ArrayList<>();
        
        for(int[] interval: intervals){
            int start_idx = interval[0];
            int end_idx = interval[1];
            
            for(int i=start_idx; i<=end_idx; i++){
                answer.add(arr[i]);
            }
        }
        
        return answer;
    }
}