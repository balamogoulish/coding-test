import java.util.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        // 1) int[] -> Integer[] (오토박싱)
        Integer[] arr = new Integer[numlist.length];
        for (int i = 0; i < numlist.length; i++) arr[i] = numlist[i];

        // 2) n과의 거리 오름차순, 거리 같으면 더 큰 수 먼저
        Arrays.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int d1 = Math.abs(o1 - n);
                int d2 = Math.abs(o2 - n);
                if (d1 == d2) return o2 - o1; // 내림차순
                return d1 - d2;               // 오름차순
            }
        });

        // 3) Integer[] -> int[] (언박싱) 후 반환
        int[] answer = new int[arr.length];
        for (int i = 0; i < arr.length; i++) answer[i] = arr[i];
        return answer;
    }
}
