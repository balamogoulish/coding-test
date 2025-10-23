import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        HashMap<Integer, ArrayList<Integer>> tree = new HashMap<>();
        int answer = n+1;
        
        for(int i=1; i<=n; i++) {
            ArrayList<Integer> list = new ArrayList<>();
            tree.put(i, list);
        }
        
        for(int[] w: wires){
            ArrayList<Integer> l1 = new ArrayList<>();
            ArrayList<Integer> l2 = new ArrayList<>();
            
            l1 = tree.get(w[0]);
            l1.add(w[1]);
            l2 = tree.get(w[1]);
            l2.add(w[0]);
        }
        
        //연결을 하나씩 끊어보고 각각 차이를 비교
        for(int[] w: wires){
            
            //1. w[0], w[1]의 연결 끊음
            ArrayList<Integer> l1 = new ArrayList<>();
            ArrayList<Integer> l2 = new ArrayList<>();
            
            l1 = tree.get(w[0]);
            l2 = tree.get(w[1]);
            if(l1.contains(w[1])) l1.remove(Integer.valueOf(w[1]));
            if(l2.contains(w[0])) l2.remove(Integer.valueOf(w[0]));
            
            //2. w[0]과 w[1]을 시작점으로 하는 트리 크기 구함
            int t1_size = treeSize(tree, w[0]);
            int t2_size = treeSize(tree, w[1]);
            answer = Math.min(answer, Math.abs(t1_size- t2_size));
            

            //3. 원상 복구하기
            l1.add(w[1]);
            l2.add(w[0]);           
            
        }
        
        
        return answer;
    }
    
    //주어진 트리의 크기 구하는 함수
    private int treeSize(HashMap<Integer, ArrayList<Integer>> tr, int start){
        Queue<Integer> q = new LinkedList<>();
        List<Integer> visited = new ArrayList<>();
        q.offer(start);
        visited.add(start);
        
        while(!q.isEmpty()){
            int curr = q.poll();
            for(int nxt: tr.get(curr)){
                if(!visited.contains(nxt)){
                    q.offer(nxt);
                    visited.add(nxt);
                }
            }
        }
        return visited.size();
        
    }
}