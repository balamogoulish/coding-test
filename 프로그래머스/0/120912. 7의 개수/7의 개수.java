class Solution {
    public int solution(int[] array) {
        int answer = 0;
        
        for(int x: array){
            String s = Integer.toString(x);
            for(char c: s.toCharArray()){
                if(c=='7') answer++;
            }
        }
        return answer;
    }
}