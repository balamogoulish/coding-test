class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n+1];
        
        int x = 1;
        for(int i=1; i<=n; i++){
            while(true){
                if(x%3==0 || Integer.toString(x).contains("3")) x++;
                else break;
            } 
            arr[i] = x++;
        }
        answer = arr[n];
        return answer;
    }
}