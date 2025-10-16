import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        char[] arr;
        HashMap<Character, Integer> hm = new HashMap<>();
        
        for(char c : s.toCharArray()){
            if(hm.containsKey(c)){
                hm.replace(c, hm.get(c)+1);
            } else{
                hm.put(c, 1);
            }
        }
        
        for(Character key: hm.keySet()){
            if(hm.get(key)==1) answer+=key;
        }
        arr = new char[answer.length()];
        for(int i=0; i<answer.length(); i++) arr[i] = answer.charAt(i);
        
        Arrays.sort(arr);
        answer="";
        for(char c: arr) answer+=c; 
        
        
        
        return answer;
    }
}