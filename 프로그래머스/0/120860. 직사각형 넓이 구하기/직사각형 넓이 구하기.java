import java.util.*;

class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        int w = 0;
        int h = 0;
        for(int i=0; i<4; i++){
            for(int j=i+1; j<4; j++){
                w = Math.max(w, Math.abs(dots[i][0] - dots[j][0]));
                h = Math.max(h, Math.abs(dots[i][1] - dots[j][1]));
            }
        }
        answer = w*h;
        return answer;
    }
}