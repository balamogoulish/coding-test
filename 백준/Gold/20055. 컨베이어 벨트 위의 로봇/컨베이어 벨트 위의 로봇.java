import java.util.*;

/**
 * 올리는 위치: 0
 * 내리는 위치: N-1
 * - 가장 먼저 벨트에 올라간 로봇부터 -> 로봇이 올라간 순서와 위치를 저장할 수 있어야 함 => deque
 */

public class Main {
    static int N;
    static int K;
    static boolean[] is_robot;
    static int[] lives;
    static Deque<Integer> robot_order;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();
        lives = new int[2*N]; //lives[i]: i칸의 내구성
        for(int i=0; i<2*N; i++) lives[i] = sc.nextInt();
        robot_order = new LinkedList<>(); //로봇을 올린 순서
        is_robot = new boolean[2*N]; //is_robot[i]: i칸에 로봇이 들어있는 지 여부
        int[] idx = new int[2*N];
        for(int i=0; i<2*N; i++) idx[i]=i;

        int up_id = 0; //올리는 위치
        int down_id = N-1; //내리는 위치
        int cnt = 0;
        while(K>0){
            cnt++;
            //1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
            rotate(idx);
            //1-1. 로봇이 내리는 위치에 도달하면 내린다. 가장 먼저 벨트에 올라간 로봇이 내리는 위치에 도달할 가능성이 있다.
            if(!robot_order.isEmpty() && is_robot[idx[down_id]]){
                robot_order.pollFirst();
                is_robot[idx[down_id]] = false;
            }

            //2. 가장 먼저 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
            Deque<Integer> tmp = new LinkedList<>();
            while(!robot_order.isEmpty()){
                int curr = robot_order.pollFirst();
                int nxt = is_able_to_move(curr);
                if(idx[down_id]==nxt){
                    is_robot[nxt] = false;
                }else tmp.offerLast(nxt);
            }
            robot_order = tmp;

            //3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
            if(lives[idx[up_id]]>0){
               lives[idx[up_id]]--;
               if(lives[idx[up_id]]==0) K--;
               is_robot[idx[up_id]] = true;
               robot_order.offerLast(idx[up_id]);
            }
        }
        System.out.println(cnt);
    }

    //t 칸 회전한 인덱스
    private static void rotate(int[] idx){
        for(int i=0; i<2*N; i++){
            idx[i] = (idx[i]+(2*N-1))%(2*N);
        }
    }

    //로봇 이동 가능시, 이동 후 다음 칸 반환
    private static int is_able_to_move(int curr){
        int nxt = (curr+1)%(2*N);
        if(!is_robot[nxt] && lives[nxt] > 0){
            is_robot[curr] = false;
            is_robot[nxt] = true;
            lives[nxt]--;
            if(lives[nxt]==0) K--;
            return nxt;
        }
        return curr;
    }
}
