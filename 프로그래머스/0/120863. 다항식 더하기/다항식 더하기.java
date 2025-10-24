class Solution {
    static int x=0;
    static int n=0;
    public String solution(String polynomial) {
        String answer = "";
        for(String s: polynomial.split(" ")){
            if(s.equals("x")) x+=1;
            else if(s.equals("+")) continue;
            else calculate(s);
        }
        if(x>0 && n>0) {
            if(x>1) answer= Integer.toString(x)+"x";
            else answer = "x";
            answer +=" + "+Integer.toString(n);
        }
        else if(x>0){
            if(x>1) answer= Integer.toString(x)+"x";
            else answer = "x";
        } else{
            answer =Integer.toString(n);
        }
        return answer;
    }
    
    void calculate(String str){
        String prev = "";
        for(char c: str.toCharArray()){
            if(c=='x') {
                x+=Integer.parseInt(prev);
                return;
            }
            else prev+=c;
        }
        n+=Integer.parseInt(prev);
    }
}