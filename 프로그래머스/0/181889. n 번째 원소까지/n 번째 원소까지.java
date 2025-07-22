import java.util.*;

class Solution {
    public List<Integer> solution(int[] num_list, int n) {
        List<Integer> nums = new ArrayList<>();
        for(int num: num_list){
            nums.add(num);
        }
        
        return nums.subList(0, n);
    }
}