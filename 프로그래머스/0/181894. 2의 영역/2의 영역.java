import java.util.*;

class Solution {
    public List solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        
        int start_idx=-1;
        int end_idx=-1;
        
        for(int i=0; i<arr.length; i++){
            if(arr[i]==2){
                if(start_idx==-1){ //2가 처음 나온 경우
                    start_idx=i;
                } else{ //2가 처음이 아닌 경우
                    end_idx=i;
                }
            }
        }
        
        if(start_idx==-1){ //2가 한 번도 나오지 않은 경우
            answer.add(-1);
        } else if(end_idx==-1){ //2가 한 번만 나온 경우
            answer.add(arr[start_idx]);            
        } else{ //2가 여러 개인 경우
            for(int i=start_idx; i<=end_idx; i++){
                answer.add(arr[i]);
            }
        }
        
        return answer;
    }
}