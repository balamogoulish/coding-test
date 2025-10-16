class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        
        for(String x:s1){
            if(isContains(x, s2)) answer++;
        }
        return answer;
    }
    
    boolean isContains(String str, String[] arr){
        for(String s:arr){
            if(str.equals(s)) return true;
        }
        return false;
    }
}