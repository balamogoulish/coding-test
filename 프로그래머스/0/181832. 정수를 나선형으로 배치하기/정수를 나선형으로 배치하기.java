import java.util.*;

class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        
        int cx = 0;
        int cy = 0;
        int d = 0;
        
        for(int i=1; i<=n*n; i++){
            answer[cy][cx] = i;
            
            int nx = dx[d]+cx;
            int ny = dy[d]+cy;
            
            //범위 밖이거나 이미 채워진 경우 방향 전환
            if(nx<0 || nx>=n || ny<0 || ny>=n || answer[ny][nx]!=0){
                d=(d+1)%4;
                nx = dx[d]+cx;
                ny = dy[d]+cy;
            }
            cx = nx;
            cy = ny;
        }
        return answer;
    }
}