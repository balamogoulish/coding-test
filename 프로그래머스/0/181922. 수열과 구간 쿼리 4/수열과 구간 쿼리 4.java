class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        
        for(int x=0; x<queries.length; x++){
            int s = queries[x][0];
            int e = queries[x][1];
            int k = queries[x][2];
            
            for(int i=s; i<=e; i++){
                arr[i] = i%k==0 ? arr[i]+1 : arr[i];
            }
        }
        return arr;
    }
}