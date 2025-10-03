import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> st = new Stack<>();

        //"(" -> push
        //")" -> pop -> "("이 안 나오면 false
        
        for(char c: s.toCharArray()){
            if('('== c) st.push('(');
            else {
                if(st.isEmpty()) return false;
                if(st.pop()!='(') return false;
            }
        }
        if(!st.isEmpty()) return false;
        return answer;
    }
}