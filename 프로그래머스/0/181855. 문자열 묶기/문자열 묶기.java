import java.util.*;

class Solution {
    public int solution(String[] strArr) {
        Map<Integer, Integer> hm = new HashMap<>();

        for (String str : strArr) {
            int key = str.length();
            hm.put(key, hm.getOrDefault(key, 0) + 1);
        }

        return Collections.max(hm.values());
    }
}
