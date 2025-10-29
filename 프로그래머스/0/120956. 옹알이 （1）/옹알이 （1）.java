/**
1. aya, ye, woo, ma를 순회하면서, 시작부터 substring(0, 타겟 문자열 길이)가 같은 지 확인
2. 같은 경우, 같은 부분은 잘라서 버림
3. 다 다른 경우 다음으로 넘어감
**/

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] arr = {"aya", "ye", "woo", "ma"};
        
        for(String b: babbling){
            while(!b.isEmpty()){
                boolean valid = false;
                for(String a: arr){
                    if(b.length() < a.length()) continue;
                    String target = b.substring(0, a.length());
                    if(a.equals(target)){
                        b = b.substring(a.length());
                        valid = true;
                        // System.out.println(a+ " -> "+b);
                        break;
                    }
                }
                if(!valid) break;
            }
            
            if(b.length()==0) answer++;
        }
        return answer;
    }
}