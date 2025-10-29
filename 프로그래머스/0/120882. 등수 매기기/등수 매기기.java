import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        HashMap<Float, List<Integer>> avgs = new HashMap<>();
        for(int i=0; i<score.length; i++){
            float avg = (float)((float)(score[i][0] + score[i][1])*0.5);
            List<Integer> list = new ArrayList<>();
            if(avgs.containsKey(avg)){
                list = avgs.get(avg);
                list.add(i);
            }else{
                list.add(i);
                avgs.put(avg, list);
            }
        }
        
        List<Float> keyList = new ArrayList<>(avgs.keySet());
        keyList.sort((s1, s2) -> s2.compareTo(s1));
        int rank = 1;
        for(Float avg: keyList) {
            List<Integer> idxs = avgs.get(avg);
            // System.out.println(avg + ": "+ idxs+"============");
            int t = 0;
            for(int idx: idxs){
                answer[idx] = rank;
                // System.out.println(idx + ": "+ rank);
                t++;
            }
            rank+=t;
        }
        
        return answer;
    }
}