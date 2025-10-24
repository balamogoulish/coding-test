class Solution {
    static int answer = 0;
    static boolean[] visited; //방문 여부

    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        
        
        for(int curr=0; curr<n; curr++){
            if(!visited[curr]){
                answer++;
                dfs(curr, computers, n);
            }
        }
        
        return answer;
    }
    
    private void dfs(int curr, int[][] computers, int n){
        for(int nxt=0; nxt<n; nxt++){
            if(computers[curr][nxt]==1 && !visited[nxt]){
                visited[nxt] = true;
                dfs(nxt, computers, n);
            }
        }
    }
}