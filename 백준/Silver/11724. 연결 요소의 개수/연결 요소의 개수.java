import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static boolean visited[];
    static ArrayList<Integer>[] A;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); //정점의 개수
        int M = sc.nextInt(); //간선의 개수
        visited = new boolean[N+1];
        A = new ArrayList[N+1];
        for(int i=1; i<N+1; i++){
            A[i] = new ArrayList<Integer>();
        }
        for(int i=0; i<M; i++){
            int u = sc.nextInt();
            int v = sc.nextInt();

            A[u].add(v);
            A[v].add(u);
        }

        int count = 0;
        for(int i=1; i<N+1; i++){
            if(!visited[i]){
                count++;
                DFS(i);
            }
        }
        System.out.println(count);
    }

    private static void DFS(int i){
        if(visited[i]) {
            return;
        }
        visited[i] = true;
        for(int nxt: A[i]){
            if(!visited[nxt]){
                DFS(nxt);
            }
        }
    }
}
