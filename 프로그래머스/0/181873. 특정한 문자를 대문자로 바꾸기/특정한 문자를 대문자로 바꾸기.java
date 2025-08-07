class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
        
        for(char c: my_string.toCharArray()){
            String c_str = c+"";
            if(c_str.equals(alp)){
                c_str = c_str.toUpperCase();
            }
            answer+=c_str;
        }
        return answer;
    }
}