//slice=7, n=10 -> 10/7=1, 10%7!=0 -> 2
//slice=4, n=12 -> 12/4=3, 12%4==0 -> 3

class Solution {
    public int solution(int slice, int n) {
        return n/slice + (n%slice==0 ? 0 : 1);
    }
}