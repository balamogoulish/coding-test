import java.util.Scanner;

/**
 * N: 1~100,000: 수의 개수
 * M: 1~100,000: 줄의 개수
 * 시간제한: 0.5초 => 5천만번
 */
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long[] nums = new long[N];
        long sum = 0;
        for(int i=0; i<N; i++){
            sum+=sc.nextInt();
            nums[i]=sum;
        }

        for(int k=0; k<M; k++){
            int i=sc.nextInt();
            int j=sc.nextInt();
            if(i<2){
                System.out.println(nums[j-1]);
            } else{
                System.out.println(nums[j-1]-nums[i-2]);
            }
        }

        /** 시간 초과!!
        for(int k=0; k<M; k++){
            int i=sc.nextInt();
            int j=sc.nextInt();
            long sum = 0;
            for(int l=i; l<=j; l++){
                sum+=nums[l-1];
            }
            System.out.println(sum);
        }
         **/


    }
}
