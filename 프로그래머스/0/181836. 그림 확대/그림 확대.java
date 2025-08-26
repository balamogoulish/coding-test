import java.util.*;

class Solution {
    public List<String> solution(String[] picture, int k) {
        List<String> answer = new ArrayList<>();
        for(String row: picture){
            String new_row = "";
            for(char c: row.toCharArray()){
                String c_str = c+"";
                new_row+=c_str.repeat(k)+"";
            }
            for(int i=0; i<k; i++){
                answer.add(new_row);
            }
        }
        return answer;
    }
}