import java.util.*;

class Solution {
    
    static List<String> list;
    static char[] alphabets = {'A', 'E', 'I', 'O', 'U'};
    
    public int solution(String word) {
        int answer = 0;
        list = new ArrayList<>();
        
        //1. 가능한 문자열을 모두 만듦
        makeStr("", 0);
        //2. 문자열을 정렬함
        String[] dic = list.toArray(new String[list.size()]);
        Arrays.sort(dic);
        
        
        
        for(int i=0; i<dic.length; i++){
            if(dic[i].equals(word)) return i+1;
        }
        return answer;
    }
    
    private void makeStr(String str, int len){
        if(len==5) return;
        
        for(char c: alphabets){
            if(!list.contains(str+c)){
                makeStr(str+c, len+1);
                list.add(str+c);
            }
        }
    }
    
}