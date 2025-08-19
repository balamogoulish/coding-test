import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stk = new Stack<>();
        int i=0;
        
        while(i<arr.length){
            if(stk.size()==0){
                stk.push(arr[i]);
                i++;
            }else{
                int last = stk.pop();
                if(last==arr[i]){
                    i++;
                }else{
                    stk.push(last);
                    stk.push(arr[i]);
                    i++;
                }
            }
        }
        if(stk.size()==0){
            stk.push(-1);
        }
       return stk.stream().mapToInt(Integer::intValue).toArray();
    }
}