class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        if(arr1.length==arr2.length){
            int sum_a1 = 0;
            int sum_a2 = 0;
            for(int a1: arr1){
                sum_a1+=a1;
            }
            for(int a2:arr2){
                sum_a2+=a2;
            }
            answer = sum_a1==sum_a2 ? 0 : sum_a1>sum_a2 ? 1 : -1;
        } else{
            answer = arr1.length > arr2.length ? 1: -1;
        }
        return answer;
    }
}