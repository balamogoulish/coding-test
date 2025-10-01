import java.util.*;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> freq = new HashMap<>();
        
        for(int num: array){
            freq.merge(num, 1, Integer::sum);
        }
        
        int maxFreq = 0;
        int mode = -1;
        boolean multiple = false;
        
        for(Map.Entry<Integer, Integer> e: freq.entrySet()){
            int num = e.getKey();
            int count = e.getValue();
            
            if(count>maxFreq){
                maxFreq = count;
                mode = num;
                multiple =false;
            } else if(count == maxFreq){
                multiple = true;
            }
        }
        return multiple ? -1 : mode;
    }
}