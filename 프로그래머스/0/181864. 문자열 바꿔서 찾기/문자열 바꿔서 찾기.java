class Solution {
    public int solution(String myString, String pat) {
        String pat_ab = "";
        
        for(char c: pat.toCharArray()){
            if(c=='A'){
                pat_ab+="B";
            }else{
                pat_ab+="A";
            }
        }
        
        return myString.contains(pat_ab) ? 1 : 0;
    }
}