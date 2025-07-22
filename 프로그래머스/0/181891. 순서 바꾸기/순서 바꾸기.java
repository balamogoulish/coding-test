import java.util.*;

class Solution {
    public List solution(int[] num_list, int n) {
        List<Integer> nums = new ArrayList<>();
        for(int num: num_list){
            nums.add(num);
        }
        
        List<Integer> n_before = nums.subList(0, n);
        List<Integer> n_after = nums.subList(n, nums.size());
        
        List<Integer> answer = new ArrayList<>();
        answer.addAll(n_after);
        answer.addAll(n_before);

        return answer;
    }
}