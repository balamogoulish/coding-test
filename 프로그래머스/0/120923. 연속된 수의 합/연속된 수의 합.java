/**
num이 홀수인 경우
중앙 idx = num/2
중앙값 = total/num

num이 짝수인 경우
중앙 idx = num/2-1
중앙값 = total/num

**/

class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        int mid_idx = num/2;
        int mid_value = total/num;
        
        if(num%2==0) mid_idx--;
        
        for(int i=0; i<num; i++){
            answer[i] = mid_value + i - mid_idx;
        }
        return answer;
    }
}