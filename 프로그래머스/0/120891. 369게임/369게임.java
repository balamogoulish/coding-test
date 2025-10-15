class Solution {
    public int solution(int order) {
        int answer = 0;
        for(char c: Integer.toString(order).toCharArray()){
            int x =Character.getNumericValue(c);
            if(x%3==0 && x!=0) answer++;
        }
        return answer;
    }
}