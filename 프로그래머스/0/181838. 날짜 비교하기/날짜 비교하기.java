class Solution {
    public int solution(int[] date1, int[] date2) {
        int date1_int = Integer.parseInt(Integer.toString(date1[0])+Integer.toString(date1[1])+Integer.toString(date1[2]));
        int date2_int = Integer.parseInt(Integer.toString(date2[0])+Integer.toString(date2[1])+Integer.toString(date2[2]));
        return date1_int<date2_int ? 1: 0;
    }
}