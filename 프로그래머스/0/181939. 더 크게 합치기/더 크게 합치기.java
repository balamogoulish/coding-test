class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String str_a = Integer.toString(a);
        String str_b = Integer.toString(b);
        
        int ab = Integer.parseInt(str_a+str_b);
        int ba = Integer.parseInt(str_b+str_a);
        
        return ab>ba ? ab: ba;
    }
}