import java.util.Scanner;

/**
 * N: 1~10,000,000 (천만)
 * Q. 연속된 자연수의 합으로 나타내는 개수는?
 * 투포인터 문제
 * start_index, end_index를 0에서 시작함
 * N보다 작으면 end_index를 우측으로 이동
 * N보다 크면 end_index를 좌측으로 이동
 * start_index가 end_index보다 커지면 끝!
 */
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int answer = 1;

        int start_index = 1;
        int end_index = 1;
        int sum = 1;
        while(end_index<N){
            if(sum==N){
                answer++;;
                end_index++;
                sum+=end_index;
            } else if(sum>N){
                sum-=start_index;
                start_index++;
            } else{
                end_index++;
                sum+=end_index;
            }
        }
        System.out.println(answer);
    }
}