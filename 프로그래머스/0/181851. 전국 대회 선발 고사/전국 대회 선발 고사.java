/**
- key: 학생번호, value: 등수 => Map 생성 (attendance가 true인 학생만)
- value 기준으로 정렬
- top 3 학생을 뽑아 정답 계산 및 출력
**/

import java.util.*;
import java.util.stream.Collectors; 

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        Map<Integer, Integer> rankers = new HashMap<>();
        
        for(int i=0; i<rank.length; i++){
            if(attendance[i]){
                rankers.put(i, rank[i]);
            }
        }
         List<Integer> top = rankers.entrySet().stream()
                .sorted(Map.Entry.comparingByValue()) // 등수 낮은 순
                .limit(3)
                .map(Map.Entry::getKey)               // 학생번호
                .collect(Collectors.toList()); 
        
        return top.get(0)*10000+top.get(1)*100+top.get(2);
    }
}