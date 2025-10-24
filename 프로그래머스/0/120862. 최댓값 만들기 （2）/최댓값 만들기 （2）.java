/**
최댓값 만들기
양수 최댓값 두개 곱
음수 최댓값 두개 곱
1 0 0 0 -1 인 경우 -> 양수, 음수 1개씩, 나머지는 다 0인 경우, 양수 최댓값, 음수 최솟값 곱
**/

import java.util.*;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        if(numbers.length==2) return numbers[0]*numbers[1];
        
        Arrays.sort(numbers);
        int plusMax = numbers[numbers.length-1] * numbers[numbers.length-2];
        int minusMax = numbers[0] *numbers[1];
        answer = Math.max(plusMax, minusMax);
        return answer;
    }
}