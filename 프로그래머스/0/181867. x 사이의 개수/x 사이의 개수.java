import java.util.*;

class Solution {
    public List solution(String myString) {
        List<Integer> answer = new ArrayList<>();
        
        String[] splitedStr = myString.split("x");
 
        for(String str: splitedStr){
            answer.add(str.length());
        }
        if(myString.charAt(myString.length()-1)=='x'){
            answer.add(0);   
        }
        return answer;
    }
}