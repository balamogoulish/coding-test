class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        answer[1] = denom1 * denom2;
        answer[0] = numer1 * denom2 + numer2 * denom1;
        
        int x = gcd(answer[1], answer[0]);
        
        answer[1] = answer[1]/x;
        answer[0] = answer[0]/x;
        
        
        return answer;
    }
    
    public static int gcd(int a, int b){
        if(b==0) return a;
        return gcd(b, a%b);
    }
}