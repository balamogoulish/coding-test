class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        
        for(int i=0; i<code.length(); i++){
             char curr = code.charAt(i);
            if(mode==0){
                if(curr=='1'){
                    mode=1;
                }else if(i%2==0){
                    answer+=curr;
                }
            } else{
                if(curr=='1'){
                    mode=0;
                }else if(i%2==1){
                    answer+=curr;
                }
            }
        }
        if(answer.length()==0){
            return "EMPTY";
        }
        return answer;
    }
}