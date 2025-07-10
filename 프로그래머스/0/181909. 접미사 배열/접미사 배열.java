import java.util.*;

class Solution {
    public List solution(String my_string) {
        List<String> answer = new ArrayList<>();
        
        for(int i=0; i<my_string.length(); i++){
            String str = my_string.substring(i);
            answer.add(str);
        }
        Collections.sort(answer);
        return answer;
    }
}