class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for (int num : num_list) {
            int n = 0;
            if (num < 2) {
                n=0;
            } else if (num < 4) {
                n=1;
            } else if (num < 8) {
                n=2;
            } else if (num < 16) {
                n=3;
            } else {
                n=4;
            }
            System.out.println(num+":"+n);
            answer+=n;
        }
        return answer;
    }
}