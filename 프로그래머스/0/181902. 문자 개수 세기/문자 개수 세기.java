class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52]; 
        for(char c : my_string.toCharArray()){
            int index = (int)c>90 ? (int)c-71: (int)c-65;
            answer[index]+=1;
        }
        return answer;
    }
}