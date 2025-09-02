import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); //연산의 개수
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((o1, o2)->{
            int first_abs = Math.abs(o1);
            int second_abs = Math.abs(o2);
            if(first_abs==second_abs) return o1 > o2 ? 1: -1;//절댓값이 같은 경우 음수 우선
            return first_abs - second_abs;//절댓값 작은 데이터 우선
        });
        int[] inputs = new int[N];
        for(int i=0; i<N; i++){
            inputs[i] = sc.nextInt();
        }

        for(int x : inputs){
            if (x == 0) {
                if (minHeap.isEmpty()) {
                    System.out.println(0);
                } else {
                    System.out.println(minHeap.poll());
                }
            } else {
                minHeap.add(x);
            }
        }
    }
}
