import java.util.*;

class Solution {
    public long solution(String numbers) {
        ArrayList<String> words = new ArrayList<>(Arrays.asList("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"));
        long answer = 0;
        String ans = "";
        
        String prev = "";
        for(char c: numbers.toCharArray()){
            prev+=c;
            int idx = words.indexOf(prev);
            if(idx>=0){
                ans+= Integer.toString(idx);
                prev = "";
            }
        }
        
        answer = Long.parseLong(ans);
        
        
        return answer;
    }
}