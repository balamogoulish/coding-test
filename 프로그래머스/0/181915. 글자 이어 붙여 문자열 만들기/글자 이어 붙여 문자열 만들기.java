import java.util.*;

class Solution {
    public String solution(String my_string, int[] index_list) {
        String answer = "";
        char[] charArr = my_string.toCharArray();
        
        for(int i = 0; i<index_list.length; i++){
            answer+=charArr[index_list[i]];
        }
        return answer;
    }
}