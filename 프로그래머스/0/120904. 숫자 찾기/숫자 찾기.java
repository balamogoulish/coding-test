class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String num_str = Integer.toString(num);
        
        for(int i=0; i<num_str.length(); i++){
            if(Character.getNumericValue(num_str.charAt(i)) == k) return i+1;
        }
        return answer;
    }
}