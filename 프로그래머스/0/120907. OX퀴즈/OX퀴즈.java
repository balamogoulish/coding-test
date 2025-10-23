class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        
        for(int i=0; i<quiz.length; i++){
            String[] prefix = quiz[i].split(" ");
            int result = calculate(Integer.parseInt(prefix[0]), Integer.parseInt(prefix[2]), prefix[1]);
            if(result == Integer.parseInt(prefix[4])) answer[i] = "O";
            else answer[i] = "X";
        }
        return answer;
    }
    
    int calculate(int x, int y, String op){
        if(op.equals("+")) return x+y;
        else return x-y;
    }
}