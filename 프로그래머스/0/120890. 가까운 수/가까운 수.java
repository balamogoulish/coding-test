import java.util.*;

class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        
        Arrays.sort(array);
        
        int min_x = -101;
        int max_x = 101;
        for(int i=0; i<array.length; i++){
            int x = array[i];
            //x가 n보다 작은 경우 -> min_x를 갱신
            if(x < n) min_x = x;
            
            //x가 n보다 큰 경우 -> max_x를 갱신 & break;
            else if(x > n) {max_x = x; break;}
            
            //x==n인 경우, x return
            else return x;
        }
        
        return n-min_x <= max_x-n ? min_x : max_x;
    }
}