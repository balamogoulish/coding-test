class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(char c: my_string.toCharArray()){
            if(answer.contains(c+"")) continue;
            answer+= c+"";
        }
        return answer;
    }
}