class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int size_arr = num2-num1+1;
        int[] answer = new int[size_arr];
        System.arraycopy(numbers, num1, answer, 0, size_arr);
        return answer;
    }
}