

class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] arr = s.split(" ");
        
        int prev = 0;
        for(String a : arr) {
            if(a.equals("Z")) {
                answer-=prev;
                continue;
            }
            prev = Integer.parseInt(a);
            answer+=prev;
        }
        return answer;
    }
}