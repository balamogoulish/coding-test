class Solution {
    public int solution(int a, int b) {
        int answer = 1;
        int x = gcd(a, b);
        b/=x;
        
        while(b>1){
            if(b%2==0) b/=2;
            else if(b%5==0) b/=5;
            else return 2;
        }
        return answer;
    }
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }

}