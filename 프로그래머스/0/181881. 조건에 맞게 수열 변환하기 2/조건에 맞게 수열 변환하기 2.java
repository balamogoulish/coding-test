class Solution {
    public int solution(int[] arr) {
        int x = 0;
        boolean isAnswer = false;
        
        while(isAnswer==false){
            x+=1;
            isAnswer = true;
            for(int i=0; i<arr.length; i++){
                int n = arr[i];
                if(n>=50 && n%2==0){
                    n/=2;
                } else if(n<50 && n%2!=0){
                    n=n*2+1;
                }
                if(arr[i]!=n){
                    isAnswer = false;
                }
                arr[i]=n;
            }
        }
        
        
        return x-1;
    }
}