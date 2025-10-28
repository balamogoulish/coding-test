class Solution {
    public String solution(String bin1, String bin2) {
        String answer = "";
        
        int b1 = Integer.parseInt(bin1,2);
        int b2 = Integer.parseInt(bin2,2);
        answer = Integer.toBinaryString(b1+b2);
        return answer;
    }
}