class Solution {
    public int solution(int M, int N) {
        int answer = 0;
        int m = 0;
        int n = 0;
        if(M==1 && N==1) return answer;
        
        if(M>=N){
            //N부터 잘라야 함
            n = N-1;
            m = (M-1)*N;
        } else{
            m = M-1;
            n = (N-1)*M;
        }
        answer = m+n;
        return answer;
    }
}