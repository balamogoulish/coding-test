class Solution {
    
    static int[] curr = {0,0};
    static int limit_x, limit_y;
    
    public int[] solution(String[] keyinput, int[] board) {

        limit_x = board[0]/2;
        limit_y = board[1]/2;
        
        for(String order: keyinput){
            move(order);
        }
        return curr;
    }
    
    void move(String order){
        switch(order){
            case "up":
                if(curr[1] < limit_y) curr[1]+=1;
                break;
            case "down":
                if(curr[1] > limit_y*-1) curr[1]-=1;
                break;
            case "right":
                if(curr[0] < limit_x) curr[0]+=1;
                break;
            case "left":
                if(curr[0] > limit_x*-1) curr[0]-=1;
                break;
        }
    }
}