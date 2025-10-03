import java.util.Scanner;

public class Main {

    static int N, M;
    static boolean[] V; //숫자 사용 여부
    static int[] S; //수열 정보 저장
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        S = new int[N];
        V = new boolean[N];
        backtracking(0);
    }

    private static void backtracking(int len){
        if(len==M){ //M개 뽑은 경우 출력, 반환
            printArray();
            return;
        }
        for(int i=0; i<N; i++){
            if(!V[i]){
                V[i] = true; //방문 처리
                S[len] = i;
                backtracking(len+1);
                V[i] = false;

            }
        }
    }

    private static void printArray(){
        for(int i=0; i<M; i++){
            System.out.print(S[i]+1+" ");
        }
        System.out.println();
    }
}
