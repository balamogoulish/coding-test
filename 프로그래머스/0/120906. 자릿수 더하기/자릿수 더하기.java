class Solution {
    public int solution(int n) {
        int answer = 0;
        for(char c: Integer.toString(n).toCharArray()){
            int x = Character.getNumericValue(c);
            answer+=x;
        }
        return answer;
    }
}