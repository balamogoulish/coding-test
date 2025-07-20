import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr, int[] query) {
        List<Integer> list = new ArrayList<>();
        for (int num : arr) {
            list.add(num);
        }

        for (int i = 0; i < query.length; i++) {
            int idx = query[i];
            if (i % 2 == 0) {
                // 짝수 인덱스 → 뒷부분 자르기
                list = list.subList(0, idx + 1);
            } else {
                // 홀수 인덱스 → 앞부분 자르기
                list = list.subList(idx, list.size());
            }
        }

        return list;
    }
}
