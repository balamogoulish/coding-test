class Solution {
    public int solution(String number) {
        int answer = 0;
        
        for(char c: number.toCharArray()){
            int num = Integer.parseInt(c+"");
            answer+=num;
        }
        
        return answer%9;
    }
}