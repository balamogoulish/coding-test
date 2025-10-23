/**
w:4, h:3   -> 테두리 10 (4*2 + 3*2 -4),
w:3, h:3   -> 테두리 8  (3*2 + 3*2 -4)
w:8, h:6   -> 테두리 24 (w*2 + h*2 -4)

**/
import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        int size = brown+yellow;
        
        for(int h=1; h<=(int)Math.sqrt(size); h++){
            if(size%h==0){
                int w = size/h;
                if(brown== (w+h)*2-4){
                    answer[0] = w;
                    answer[1] = h;
                    break;
                }
            }
        }
        return answer;
    }
}