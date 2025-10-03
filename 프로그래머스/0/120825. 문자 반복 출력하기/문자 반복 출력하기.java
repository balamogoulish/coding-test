class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        for(char c:my_string.toCharArray()){
            String c_str = c+"";
            answer+=c_str.repeat(n);
        }
        return answer;
    }
}