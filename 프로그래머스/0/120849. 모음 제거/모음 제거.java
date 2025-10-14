import java.util.*;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        ArrayList<Character> aeiou = new ArrayList<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        
        for(char c: my_string.toCharArray()){
            if(aeiou.contains(c)) continue;
            answer+=c;
        }
        return answer;
    }
}