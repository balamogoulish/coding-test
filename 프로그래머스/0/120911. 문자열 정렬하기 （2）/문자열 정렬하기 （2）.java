import java.util.*;
class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] arr = new char[my_string.length()];
        
        for(int i=0; i<my_string.length(); i++){
            arr[i] = Character.toLowerCase(my_string.charAt(i));
        }
        
        Arrays.sort(arr);
        for(char c:arr) answer+=c;
        return answer;
    }
    
    
}