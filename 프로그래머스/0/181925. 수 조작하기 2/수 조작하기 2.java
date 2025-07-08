class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        
        int prev = numLog[0];
        for(int i=1; i<numLog.length; i++){
            int num = numLog[i];
            
            if (prev+1==num) answer+="w";
            else if (prev-1==num) answer+="s";
            else if (prev+10==num) answer+="d";
            else if (prev-10==num) answer+="a";
            prev=num;
        }
        
        return answer;
    }
}