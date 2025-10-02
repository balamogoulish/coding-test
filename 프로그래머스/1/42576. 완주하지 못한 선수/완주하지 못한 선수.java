import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        for(int i=0; i<completion.length; i++){
            String p = participant[i];
            String c = completion[i];
            
            if(!p.equals(c)) {
                return p;
            }
        }
        return participant[participant.length-1];
    }
}