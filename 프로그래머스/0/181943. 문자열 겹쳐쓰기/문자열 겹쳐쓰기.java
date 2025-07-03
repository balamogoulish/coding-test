class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        
        String prev_my = my_string.substring(0, s);
        String after_my = my_string.substring(overwrite_string.length()+s);
        
        return prev_my+overwrite_string+after_my;
    }
}