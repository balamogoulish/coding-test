import java.util.*;

class Solution {
    public List<String> solution(String myStr) {
        String[] split_a = myStr.split("a");
        List<String> split_ab = new ArrayList<>();
        List<String> split_abc = new ArrayList<>();
        
        for(String str: split_a){
            if(!str.equals("")){
                String[] tmp = str.split("b");
                for(String t: tmp){
                    if(!t.equals("")){
                        split_ab.add(t);
                    }
                    
                }
            }
        }
        for(String str: split_ab){
            String[] tmp = str.split("c");
            for(String t:tmp){
                if(!t.equals("")){
                    split_abc.add(t);
                }
            }
        }
        if(split_abc.size()==0){
            return new ArrayList<String>(List.of("EMPTY"));
        }
        return split_abc;
    }
}