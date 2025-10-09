import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] strs = new String[numbers.length];
        for(int i=0; i<numbers.length; i++) strs[i] = Integer.toString(numbers[i]);
        Arrays.sort(strs, (o1, o2)-> o2.repeat(4).compareTo(o1.repeat(4)));
        
        for(String s: strs) answer+=s;
        return answer.charAt(0)=='0' ? "0" : answer;
    }
}