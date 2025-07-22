import java.util.*;

class Solution {
    public List<String> solution(String[] str_list) {
        List<String> answer = new ArrayList<>();
        
        for(int i=0; i<str_list.length; i++){
            if(str_list[i].equals("l")){//왼쪽 문자열 반환
                answer = Arrays.asList(str_list).subList(0,i);
                break;
            } else if(str_list[i].equals("r")){//오른쪽 문자열 반환
                answer = Arrays.asList(str_list).subList(i+1, str_list.length);
                break;
            }
        }
        return answer;
    }
}