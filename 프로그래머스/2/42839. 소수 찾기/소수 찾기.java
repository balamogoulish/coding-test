import java.util.*;

class Solution {
    static int answer=0;
    static String num_str;
    static List<Integer> primes = new ArrayList<>();
    public int solution(String numbers) {
        num_str = numbers;
        List<Integer> visited = new ArrayList<>();
        permutate(visited, numbers.length());
        return answer;
    }
    
    
    //조합
    private void permutate(List<Integer> visited, int target_len){
        String x_str = "";
        for(int idx: visited){
            x_str+=num_str.charAt(idx);
        }
        if(x_str.length()>0 && !primes.contains(Integer.parseInt(x_str)) &&isPrime(Integer.parseInt(x_str))) {
            primes.add(Integer.parseInt(x_str));
            answer++;
        }
        
        if(visited.size()>target_len){    
            return;
        }
        
        //visited 크기가 target_len보다 작은 경우, 아직 방문하지 않은 곳을 추가
        for(int idx=0; idx<target_len; idx++){
            if(!visited.contains(idx)){
                List<Integer> visited_copy = new ArrayList<>(visited);
                visited_copy.add(idx);
                permutate(visited_copy, target_len);
            }
        }
    }
    
    //소수 검사
    private boolean isPrime(int x){
        if(x==0 || x==1) return false;
        for(int i=2; i<=(int)Math.sqrt(x); i++){
            if(x%i==0) return false;
        }
        return true;
    }
}