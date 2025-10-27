import java.util.*;

class Solution {
    public int solution(String my_string) {
        int answer = 0;
        
        String prev = "";
        for(char c:my_string.toCharArray()){
            if(Character.isDigit(c)){
                prev+=c;
            }else{
                if(!prev.isEmpty()){
                    answer+=Integer.parseInt(prev);
                    prev="";
                }
            }
        }
        if(!prev.isEmpty()){
                    answer+=Integer.parseInt(prev);
                }
        return answer;
    }
}