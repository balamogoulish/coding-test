class Solution {
    public int solution(int[][] lines) {
        int[] count = new int[201];
        for(int i=0; i<3; i++) {
            for(int j=lines[i][0]+100; j<lines[i][1]+100; j++) {
                count[j]++;
            }
        }
        
        int answer = 0;
        for(int i=0; i<count.length; i++) {
            if(count[i] > 1) {
                answer++;
            }
        }
        return answer;
    }
}