import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        Integer[] arr = new Integer[numbers.length];
        for(int i=0; i<numbers.length; i++){
            arr[i] = (Integer) numbers[i];
        }
        Arrays.sort(arr, Collections.reverseOrder());
        return arr[0] *arr[1];
    }
}