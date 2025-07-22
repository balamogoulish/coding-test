import java.util.*;

class Solution {
    public List solution(int[] num_list, int n) {
        List<Integer> answer = new ArrayList<>();
        for(int num: num_list){
            answer.add(num);
        }
        answer = answer.subList(n-1, answer.size());
        
        return answer;
    }
}