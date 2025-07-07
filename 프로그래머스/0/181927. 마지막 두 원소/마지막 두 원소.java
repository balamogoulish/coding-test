class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length+1];
        
        int last = num_list[num_list.length-1];
        int last_before = num_list[num_list.length-2];
        int add = 0;
        
        for (int i=0; i<num_list.length; i++){
            answer[i]=num_list[i];
        }
        if(last>last_before){
            add = last-last_before;
        }else{
            add = last*2;
        }
        
        answer[num_list.length]=add;
        return answer;
    }
}