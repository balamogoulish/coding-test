class Solution {
    public String solution(String myString) {
        String answer = "";
        
        for(char x: myString.toCharArray()){
            int x_int = x;
            int l_int = 'l';
            if(x_int<l_int){
                answer+="l";
            } else{
                answer+=x+"";
            }
        }
        return answer;
    }
}