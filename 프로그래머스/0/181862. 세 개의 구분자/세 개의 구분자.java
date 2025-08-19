class Solution {
    public String[] solution(String myStr) {
        myStr = myStr.replaceAll("[abc]+", ",");
        myStr = myStr.charAt(0) == ',' ? myStr.substring(1): myStr; //,로 시작하는 경우 , 버림
        myStr = myStr.equals("") ? "EMPTY" : myStr;
        
        return myStr.split(",");
    }
}