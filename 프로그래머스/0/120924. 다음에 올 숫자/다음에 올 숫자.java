class Solution {
    public int solution(int[] common) {
        int answer = 0;
        
        if(common[1] - common[0] == common[2] - common[1]){ //등비 수열인 경우
            int diff = common[1]-common[0];
            answer = common[common.length-1]+diff;
        } else{
            int diff = common[1]/common[0];
            answer = common[common.length-1]*diff;
        }
        return answer;
    }
}