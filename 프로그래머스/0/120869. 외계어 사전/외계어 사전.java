class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;
        for(String d: dic){
            boolean ok = true;
            for(String s: spell){
                if(!d.contains(s)){
                    ok = false;
                    break;
                }
            }
            if(ok){
                answer=1;
                break;
            }
        }
        return answer;
    }
}