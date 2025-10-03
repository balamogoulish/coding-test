import java.util.Scanner;

/**
 * Queen은 상하좌우, 대각선 방향ㅇ로 이동 가능
 */

public class Main {
    static int N;
    static int[] board;
    static int answer;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        board = new int[N];
        backtracking(0);
        System.out.println(answer);
    }

    private static void backtracking(int row){
        if(row==N){
            answer++;
            return;
        }
        for(int i=0; i<N; i++){
            board[row] = i;
            if(check(row)){
                backtracking(row+1);
            }
        }
    }

    private static boolean check(int row){
        for(int i=0; i<row; i++){
            if(board[i] == board[row]) return false;
            if(Math.abs(row-i) == Math.abs(board[row]-board[i])) return false;
        }
        return true;
    }
}
