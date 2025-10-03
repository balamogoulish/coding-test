/**

**/

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hm = new HashMap<>();
        for(String[] c:clothes){
            String key = c[1];
            hm.putIfAbsent(key, 1);
            hm.replace(key, hm.get(key)+1);
        }
        for(String key: hm.keySet()){
            answer*=hm.get(key);
        }
        return answer-1;
    }
}