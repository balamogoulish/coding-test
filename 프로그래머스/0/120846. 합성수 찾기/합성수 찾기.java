class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n+1];
        
        for(int i=2; i<=n; i++){
            for(int j=1; j*i<=n; j++){
                arr[i*j]+=1;
            }
        }
        
        for(int x: arr) if(x>1) answer++;
        return answer;
    }
    
    
}