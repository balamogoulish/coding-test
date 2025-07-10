import java.util.*;

class Solution {
    public List solution(String[] intStrs, int k, int s, int l) {
       List<Integer> answer = new ArrayList<>();
        
        for(String intStr : intStrs){
            int num = Integer.parseInt(intStr.substring(s, s+l));
            if (num > k){
                answer.add(num);
            }
        }
        return answer;
    }
}