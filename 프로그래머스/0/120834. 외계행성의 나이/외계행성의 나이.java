class Solution {
    public String solution(int age) {
        String answer = "";
        for(char x: Integer.toString(age).toCharArray()){
            char c = (char)(Integer.parseInt(x+"")+97);
            answer+=c;
        }
        return answer;
    }
}