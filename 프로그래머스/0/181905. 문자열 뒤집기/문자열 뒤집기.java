import java.util.*;

class Solution {
    public String solution(String my_string, int s, int e) {        
        
        StringBuilder mid = new StringBuilder(my_string.substring(s,e+1)).reverse();
        String prev = my_string.substring(0, s);
        String nxt = my_string.substring(e+1);
        
        return prev+mid.toString()+nxt;
    }
}