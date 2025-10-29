import java.util.*;

class Solution {
    public int solution(String A, String B) {
        int answer = -1;
        StringBuilder a_sb = new StringBuilder(A);
        
        if(A.equals(B)) return 0;
        
        int cnt = 0;
        do{ 
            cnt++;
            a_sb.insert(0, a_sb.charAt(A.length()-1)+"");
            a_sb.deleteCharAt(A.length());
            
            if(a_sb.toString().equals(B)){
                answer = cnt;
                break;
            }
            System.out.println(a_sb.toString());
        }while(!a_sb.toString().equals(A));
        return answer;
    }
}