import java.util.*;

class Solution {
    public int solution(int[][] board) {
        int[] dx = {0, 0, 1, -1, 1, 1, -1, -1};
        int[] dy = {1, -1, 0, 0, 1, -1, 1, -1};
        int n = board.length;
        int answer = 0;
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(board[i][j] == 1){
                    for(int k=0; k<8; k++){
                        int nx = j+dx[k];
                        int ny = i+dy[k];
                        if(0<=nx && nx<n && 0<=ny && ny<n && board[ny][nx]==0){
                            board[ny][nx] = -1;
                        }
                    }
                }
            }
        }
        
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                if(board[j][i] == 0) answer++;
        
        return answer;
    }
}