import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> curr_q = new LinkedList<>(); //다리 위의 트럭 수
        Queue<Integer> waiting_q = new LinkedList<>(); //대기 중인 트럭 수
        int arrive_cnt = 0; //도착한 트럭 수
        int curr_cnt = 0; //다리 위의 트럭 수
        int curr_weight = 0; //다리 위의 트럭 무게
        
        int answer = 0;
        
        for(int i=0; i<bridge_length; i++){
            curr_q.add(0);
        }
        for(int truck_w:truck_weights){
            waiting_q.add(truck_w);
        }
        
        while(arrive_cnt < truck_weights.length){
            answer++;
            int c = curr_q.remove();
            if(c!=0){
                arrive_cnt++;
                curr_cnt--;
                curr_weight-=c;
            }
            
            if(curr_cnt<bridge_length && waiting_q.size()>0 && curr_weight+waiting_q.peek() <= weight){
                int n = waiting_q.remove();
                curr_cnt++;
                curr_weight+=n;
                curr_q.add(n);
            } else{
                curr_q.add(0);
            }
        }
        
        return answer;
    }
}