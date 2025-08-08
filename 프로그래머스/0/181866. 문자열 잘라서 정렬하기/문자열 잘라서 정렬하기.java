import java.util.*;

class Solution {
    public List solution(String myString) {
        List<String> answer = new ArrayList<>();
        for(String str:myString.split("x")){
            if(str.equals("")){
                continue;
            }
            answer.add(str);
        }
        Collections.sort(answer);
        
        return answer;
    }
}