import java.lang.Math;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        
        if(a==b && b==c && c==d){
            answer = 1111*a;
        } else if(a==b && b==c && c!=d){
            answer = (10*a+d)*(10*a+d);
        } else if (a==b && b==d && c!=d){
            answer = (10*a+c)*(10*a+c);
        } else if (a==c && d==c && c!=b){
            answer = (10*a+b)*(10*a+b);
        } else if (c==b && b==d && a!=d){
            answer = (10*d+a)*(10*d+a);
        } else if(a==b && d==c){
            answer =(a+c)*Math.abs(a-c);
        } else if(a==c && b==d){
            answer =(a+b)*Math.abs(a-b);
        } else if(a==d && b==c){
            answer =(a+c)*Math.abs(a-c);
        } else if(a==b){
            answer = c*d;
        } else if(a==c){
            answer = b*d;
        } else if(a==d){
            answer = b*c;
        } else if(b==c){
            answer = a*d;
        } else if(b==d){
            answer = a*c;
        } else if(c==d){
            answer = a*b;
        } else {
            int tmp = a;
            tmp = Math.min(tmp, b);
            tmp = Math.min(tmp, c);
            tmp = Math.min(tmp, d);
            answer =tmp;
        }
        
        
        
        return answer;
    }
}