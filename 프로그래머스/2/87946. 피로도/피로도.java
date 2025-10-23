/**
1. 최소 필요 피로도 <= k인 던전 선택
2. 던전 탐험 후 k=k-소모피로도, answer+=1
3. 탐험하지 않은 나머지 던전에서 1~2수행

**/


import java.util.*;
class Solution {
    
    static int[][] ds;
    static int answer=-1;
    public int solution(int k, int[][] dungeons) {
        ds = dungeons;
        
        List<Integer> visited = new ArrayList<>();
        goDungeon(visited, k, 0);
        
        return answer;
    }
    
    /**
    visited: 현재 방문한 던정
    k: 현재 피로도
    s: 현재 돌은 던전 개수
    **/
    private void goDungeon(List<Integer> visited, int k, int s){

        
        answer = Math.max(s, answer);
        if(s == ds.length){ //던전을 모두 돈 경우
            return;
        }
        for(int idx=0; idx<ds.length; idx++){
            if(!visited.contains(idx) && ds[idx][0] <= k){ //아직 탐험하지 않았고, 최소 필요 피로도 <= k이면 탐험
                List<Integer> visited_copy = new ArrayList<>(visited);
                visited_copy.add(idx);
                goDungeon(visited_copy, k-ds[idx][1], s+1);
            }
        }
    }
}