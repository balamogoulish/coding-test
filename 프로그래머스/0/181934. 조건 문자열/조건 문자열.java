class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        if(eq.equals("=")){
            if(n==m){
                return 1;
            }
        } 
        
        if(ineq.equals("<")){
            if(n<m){
                return 1;
            } else{
                return 0;
            }
        } else{
            if(n>m){
                return 1;
            } else{
                return 0;
            }
        }
    }
}