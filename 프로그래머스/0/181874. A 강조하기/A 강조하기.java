class Solution {
    public String solution(String myString) {
        String answer = "";
        
        for(char c: myString.toCharArray()){
            String str = c+"";
            if(str.equals("a")){
                answer+="A";
            } else if(Character.isUpperCase(c) && !str.equals("A")){
                answer+=str.toLowerCase();
            } else{
                answer+=str;
            }
        }
        return answer;
    }
}