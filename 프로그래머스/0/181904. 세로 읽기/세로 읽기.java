class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        int str_len = my_string.length();
        for(int i=0; i<str_len; i++){
            if((i+1)%m == c%m){
                answer+=my_string.substring(i,i+1);
            }
        }
        return answer;
    }
}