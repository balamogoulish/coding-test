import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int x=0; x<commands.length; x++){
            int i = commands[x][0];
            int j = commands[x][1];
            int k = commands[x][2];
            int[] arr = new int[j-i+1];
            System.arraycopy(array, i-1, arr, 0, j-i+1);
            
            Arrays.sort(arr);
            answer[x] = arr[k-1];
        }
        return answer;
    }
}