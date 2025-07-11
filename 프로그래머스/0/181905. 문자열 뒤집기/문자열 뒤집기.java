import java.util.*;

class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        
        String prev = my_string.substring(0, s);
        String mid = my_string.substring(s,e+1);
        String nxt = my_string.substring(e+1);
        
        answer+=prev;
        char[] mid_arr= mid.toCharArray();
        for(int i=0; i<mid_arr.length; i++){
            answer+=mid_arr[mid_arr.length-i-1];
        }
        answer+=nxt;
        
        return answer;
    }
}