import java.util.*;

class Solution {
    static boolean[][] board = new boolean[102][102];
    static boolean[][] visited = new boolean[102][102];
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    static int[] dx_n = {0, 0, -1, 1, 1, 1, -1, -1};
    static int[] dy_n = {1, -1, 0, 0, 1, -1, 1, -1};
    static int answer;
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        answer = 1000000;
        
        for(int[] r: rectangle){
            int x1 = r[0];
            int y1 = r[1];
            int x2 = r[2];
            int y2 = r[3];
            for(int x=x1*2; x<=x2*2; x++){
                for(int y=y1*2; y<=y2*2; y++) board[y][x] = true;
            }
        }
        
        int[] curr = {characterX*2, characterY*2};
        int[] tg = {itemX*2, itemY*2};
        visited[curr[1]][curr[0]] = true;
        dfs(curr, tg, 0);
        
        return answer/2;
    }
    
    void dfs(int[] curr, int[] target, int dist){
        
        for(int k=0; k<4; k++){
            int nx = curr[0]+dx[k];
            int ny = curr[1]+dy[k];
            if(nx>=1 && nx<=100 && ny>=1 && ny<=100 && !visited[ny][nx] && is_visitable(nx, ny)){
                if(nx == target[0] && ny == target[1]) {
                    System.out.println(dist+1);
                    answer = Math.min(answer, dist+1);
                } else{
                    visited[ny][nx] = true;
                    int[] nxts = {nx, ny};
                    dfs(nxts, target, dist+1);
                }
                
            }
        }
    }
    
    //갈 수 있는 지 판별하는 함수
    boolean is_visitable(int x, int y){
        if(!board[y][x]) return false;
        int cnt = 0;
        for(int k=0; k<8; k++){
            int nx = x+dx_n[k];
            int ny = y+dy_n[k];
            if(nx>=1 && nx<=100 && ny>=1 && ny<=100){
                if(board[ny][nx]) cnt++;
            }
        }
        if(cnt!=8) {
            return true;
        }
        return false;
        
    }
}