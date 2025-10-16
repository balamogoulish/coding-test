class Solution {
    public int[] solution(int[] array) {
        int[] answer = {0,0};
        int idx = 0;
        int max = -1;
        
        for(int i=0; i<array.length; i++){
            if(array[i]>max) {
                max = array[i];
                idx = i;
            }
        }
        answer[0] = max;
        answer[1] = idx;
        
        return answer;
    }
}