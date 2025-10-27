class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int l=sides[1]; //sides에서 긴 변
        int s=sides[0]; //sides에서 짧은 변
        if(sides[0]>sides[1]){
            l=sides[0];
            s=sides[1];
        }
        
        for(int i=1+l-s; i<s+l; i++){
          answer++;
        }
        return answer;
    }
}