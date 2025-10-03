import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> pb = new HashMap<>();
        for(String p: phone_book){
            pb.putIfAbsent(p, 0);
        }
        
        for(String prefix:pb.keySet()){
            for(int i=1; i<prefix.length(); i++){
                String sub_prefix = prefix.substring(0, i);
                if(pb.containsKey(sub_prefix)){
                    System.out.println(sub_prefix);
                    return false;
                }
            }
        }
        
        return answer;
    }
}