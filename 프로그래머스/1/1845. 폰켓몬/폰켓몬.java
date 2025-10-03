import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashMap<Integer, Integer> hm = new HashMap<>(); // 포켓몬 종류, 수
        for(int n:nums){
            if(!hm.containsKey(n)){ //해당 포켓몬이 새로운 종류인 경우
                answer++;
                hm.put(n, 1);
            }else{ //해당 포켓몬이 이미 있는 경우
                hm.replace(n, hm.get(n)+1);
            }
        }
        return Math.min(nums.length/2, answer);
    }
}