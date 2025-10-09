import java.util.*;
import java.util.Collections;
/**
1. 내림차순 정렬
2. 6,5,3,1,0 
    i=1 -> 1개 탐색, 6>1이므로 통과
    i=2 -> 2개 탐색, 6>2, 5>2이므로 통과
    i=3 -> 3개 탐색, 3>=3 이므로 통과
    i=4 -> 4개 탐색(citations[i-1]), 1<4이므로 불통
**/

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Integer[] arr = new Integer[citations.length];
        for(int i=0; i<citations.length; i++) arr[i] = citations[i];
        Arrays.sort(arr, (o1, o2)-> o2-o1);
        
        for(int i=1; i<=arr.length; i++){
            
            if(arr[i-1] >= i){
                answer = i;
            } else{
                break;
            }
        }
       
        return answer;
    }
}