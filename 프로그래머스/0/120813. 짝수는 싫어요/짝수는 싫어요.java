import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i=1; i<=n; i+=2){
            ans.add(i);
        }
        return ans;
    }
}