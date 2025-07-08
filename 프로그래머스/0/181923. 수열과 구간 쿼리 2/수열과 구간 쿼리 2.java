import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for(int i=0; i<queries.length; i++){
            int[] query = queries[i];
            int s = query[0];
            int e = query[1];
            int k = query[2];
            int[] arr_copy = Arrays.copyOfRange(arr, s, e+1);
            Arrays.sort(arr_copy);
            int result = 1000001;
            for(int num : arr_copy){
                if(num>k && result>num){
                    result = num;                }
            }
            answer[i] = result==1000001 ? -1 : result;
        }
        return answer;
    }
}