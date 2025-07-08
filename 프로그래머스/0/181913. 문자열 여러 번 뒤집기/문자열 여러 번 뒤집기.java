import java.util.*;

class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] answer = my_string.toCharArray();
        
        for(int[] query: queries){
            int s = query[0];
            int e = query[1];
            for (int i=0; i<=(e-s)/2; i++){
                char tmp = answer[s+i];
                answer[s+i] = answer[e-i];
                answer[e-i] = tmp;
            }
        }
        
        return new String(answer);
    }
}