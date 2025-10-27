import java.util.*;

class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        int[][] line1 = {{0,1}, {0,2}, {0,3}};
        int[][] line2 = {{2,3}, {1,3}, {1,2}};
        
        for(int i=0; i<3; i++){
            int[] l1 = line1[i];
            int[] l2 = line2[i];
            if(getLean(dots[l1[0]], dots[l1[1]]) == getLean(dots[l2[0]], dots[l2[1]])){
                answer=1;
                break;
            }
        }
        return answer;
    }
    
    private float getLean(int[] d1, int[] d2){
        return (float)Math.abs(d1[0]-d2[0]) / (float)Math.abs(d1[1]-d2[1]);
    }
}