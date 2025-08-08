class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        for(int i=0; i<=myString.length()-pat.length(); i++){
            String substr = myString.substring(i, pat.length()+i);
            if(substr.equals(pat)){
                answer+=1;
            }
        }
        return answer;
    }
}