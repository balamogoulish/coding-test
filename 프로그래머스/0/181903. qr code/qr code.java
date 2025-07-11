class Solution {
    public String solution(int q, int r, String code) {
        String answer = "";
        char[] codeArr = code.toCharArray();
        int code_len = code.length();
        
        for(int i=0; i<code_len; i++){
            if(i%q==r){
                answer+=codeArr[i];
            }
        }
        return answer;
    }
}