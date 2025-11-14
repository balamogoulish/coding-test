import java.util.*;

class Solution {
    static int answer = 10000;
    static int max_p_cnt = 0;
    static String[] ms;
    static int[] ps;
    static List<Integer> p_order = new ArrayList<>();

    public int solution(int[] picks, String[] minerals) {
        max_p_cnt = minerals.length/5;
        if(minerals.length%5>0) max_p_cnt++;
        
        ms = new String[minerals.length];
        for(int i = 0; i<minerals.length; i++) ms[i] = minerals[i];
        
        ps = new int[picks.length];
        int p_sum = 0;
        for(int i = 0; i<picks.length; i++){
            p_sum+=picks[i];
            ps[i] = picks[i];
        }
        max_p_cnt = Math.min(p_sum, max_p_cnt);
        
        dfs(0);
        
        return answer;
    }
    
    private void dfs(int cnt){
        if(max_p_cnt == cnt){
            answer = Math.min(answer, get_tired_sum(p_order));
            return;
        }
        
        for(int i=0; i<3; i++){
            if(ps[i]>0){
                ps[i]--;
                p_order.add(i);
                dfs(cnt+1);
                ps[i]++;
                p_order.remove(p_order.size()-1);
            }
        }
    }
    
    private int get_tired_sum(List<Integer> p){//곡괭이 p 배열에 대해 미네랄 배열을 캐는 피로도
        int result = 0;
        
        int p_idx=0;
        int m_idx=0;
        int tmp = 0;
        while(m_idx < ms.length && p_idx < p.size()){
            result+=get_tired(p.get(p_idx), ms[m_idx++]);
            tmp++;
            if(tmp==5){
                tmp=0;
                p_idx++;
            }
        }
        return result;
    }
    
    private int get_tired(int p, String m){//곡괭이 p에 대한 m의 피로도
        if(p==1 && m.equals("diamond")) return 5;
        if(p==2){
            if(m.equals("diamond")) return 25;
            if(m.equals("iron")) return 5;
        }
        return 1;
        
    }
}