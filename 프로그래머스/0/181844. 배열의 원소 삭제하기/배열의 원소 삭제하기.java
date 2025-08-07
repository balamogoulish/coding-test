import java.util.*;
import java.util.stream.*;

class Solution {
    public List solution(int[] arr, int[] delete_list) {
        List<Integer> answer = new ArrayList<>();
        for(int x: arr){
            if(!IntStream.of(delete_list).anyMatch(d -> d==x)){
                answer.add(x);
            }
        }
        return answer;
    }
}