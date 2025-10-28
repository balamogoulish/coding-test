class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        char k_char = (char)(k+'0');
        
        for(int n=i; n<=j; n++){
            String str = Integer.toString(n);
            for(char c:str.toCharArray()){
                if(k_char==c) answer++;
            }
        }
        return answer;
    }
}