class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] str_arr = my_string.split(" ");

        String op="";
        answer = Integer.parseInt(str_arr[0]);
        
        for(int i=1; i<str_arr.length; i++){
            if(isNumeric(str_arr[i])){
                if(op.equals("+")) answer+=Integer.parseInt(str_arr[i]);
                else if(op.equals("-")) answer-=Integer.parseInt(str_arr[i]);
            } else{
                op = str_arr[i];
            }
        }
        return answer;
    }
    
    private boolean isNumeric(String str){
        return str.chars().allMatch(Character::isDigit);
    }
}