class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String odds = "";
        String evens = "";
        
        for (int num : num_list){
            if(num%2==0){
                evens+=Integer.toString(num);
            }else{
                odds+=Integer.toString(num);
            }
        }
        
        
        return Integer.parseInt(odds)+Integer.parseInt(evens);
    }
}