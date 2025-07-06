class Solution {
    int get_sum(int n){
        int result = 0;
        int i = 1;
        while(i <= n){
            result+=i;
            i+=2;
        }
        return result;
    }
    
    int get_product(int n){
        int result = 0;
        int i = 0;
        while(i<=n){
            result+=i*i;
            i+=2;
        }
        return result;
    }
    
    public int solution(int n) {
        int answer = 0;
        if(n%2!=0){
            answer = get_sum(n);
        } else{
            answer = get_product(n);
        }
        return answer;
    }
}