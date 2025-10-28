import java.util.*;

class Solution {
    public int solution(String before, String after) {
        int answer = 1;
        char[] b = before.toCharArray();
        char[] a = after.toCharArray();
        Arrays.sort(b);
        Arrays.sort(a);
        
        for(int i=0; i<b.length; i++){
            if(b[i] != a[i]) return 0;
        }
        return answer;
    }
}