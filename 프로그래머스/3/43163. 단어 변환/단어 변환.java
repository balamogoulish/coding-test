/**
curr = begin
1. curr에서 갈 수 있는 words 탐색 -> 한 알파벳만 다르고, 방문한 적 없으면 OK
2. nxt를 방문 처리, nxt를 curr로 바꿔서, dist+1, 다시 탐색
3. curr==target이면 return
4. dist가 최소인 값 = answer
**/
import java.util.*;

class Solution {
    static String tg;
    static String[] ws;
    static int answer;
    
    public int solution(String begin, String target, String[] words) {
        answer = 100;
        tg = target;
        ws = words;
        boolean[] visited = new boolean[words.length];
        dfs(begin, 0, visited);
        
        if (answer == 100) answer = 0;
        return answer;
    }
    
    private void dfs(String curr, int dist, boolean[] visited){
        if(curr.equals(tg)) answer = Math.min(answer, dist);
        else{
            for(int i=0; i<ws.length; i++){
                String nxt = ws[i];
                if(!visited[i] && is_changeable(curr, nxt)){
                    boolean[] visited_copy = Arrays.copyOf(visited, visited.length);
                    visited_copy[i] = true;
                    dfs(nxt, dist+1, visited_copy);
                }
            }
        }
        
    }
    
    private boolean is_changeable(String curr, String nxt){
        int diff_cnt = 0;
        for(int i=0; i<curr.length(); i++){
            if(curr.charAt(i)!=nxt.charAt(i)){
                diff_cnt++;
                if(diff_cnt > 1) return false;
            } 
        }
        if(diff_cnt==1) return true;
        else return false;
    }
}