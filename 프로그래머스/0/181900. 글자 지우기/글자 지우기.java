import java.util.*;
class Solution {
    
    private boolean isContain(int[] arr, int target){
        for(int i: arr){
            if(target==i){
                return true;
            }
        }
        return false;
    }
    public String solution(String my_string, int[] indices) {
        String answer = "";
        
        for(int i = 0; i<my_string.length(); i++){
            if(!isContain(indices, i)){
                answer+=my_string.charAt(i);
            }
        }
        return answer;
    }
}