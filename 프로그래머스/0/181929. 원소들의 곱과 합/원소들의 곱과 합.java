class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int pro = 1;
        int sum_pow = 0;
        
        for(int num : num_list){
            pro*=num;
            sum_pow+=num;
        }
        if(pro<sum_pow*sum_pow){
            answer=1;
        }
        
        return answer;
    }
}