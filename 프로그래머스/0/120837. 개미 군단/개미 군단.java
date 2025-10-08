class Solution {
    public int solution(int hp) {
        int warload = hp/5;
        hp-= 5*warload;
        int soldiar = hp/3;
        hp-= 3*soldiar;
        int worker = hp;
        
        return warload+soldiar+worker;
    }
}