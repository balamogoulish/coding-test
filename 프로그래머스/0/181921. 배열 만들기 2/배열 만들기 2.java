// 첫번째 자리에 0이 들어갈 수 없음
// 0, 5 => 2^1
// 50, 55 , 00, 05
// 500, 505, 550, 555, 050, 055, 000, 005
// 5000, 5005, 5050, 5055, 5500, 5505, 5550, 5555
// 2^7 => 128
import java.util.*;

class Solution {
    public List solution(int l, int r) {
        List<Integer> answer = new ArrayList<>();
        
        for(int i=l; i<=r; i++){
            boolean flag = true;
            for(char c: (i+"").toCharArray()){
                if(c!='0'&& c!='5'){
                    flag = false;
                    break;
                }
            }
            if(flag){
                answer.add(i);
            }
        }
        if(answer.isEmpty()){
            answer.add(-1);
        }
        
        return answer;
    }
}