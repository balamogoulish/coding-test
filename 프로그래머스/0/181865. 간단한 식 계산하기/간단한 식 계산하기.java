class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String[] binomial_split = binomial.split(" ");
        
        int a = Integer.parseInt(binomial_split[0]);
        String op = binomial_split[1];
        int b = Integer.parseInt(binomial_split[2]);
        
        switch(op){
            case "+":
                answer = a+b;
                break;
            case "-":
                answer = a-b;
                break;
            case "*":
                answer = a*b;
                break;
        }
        return answer;
    }
}