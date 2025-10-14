/**
int[n+1] primes= True 선언
i = 2부터 i*x (i*x <= n) 인 primes[i*x]를 False로 변환
primes[i] = False가 아니면 이 과정을 반복 & answer에 추가
i = 2~n 반복



**/

import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] numbers = new int[n+1];
        List<Integer> primes = new ArrayList<>();
        
        for(int i=2; i<=n; i++){
            if(numbers[i]==0){ //소인수인 경우
                if(n%i==0) primes.add(i);
                for(int j=1; j*i<=n; j++){
                    numbers[i*j] +=1;
                }
            }
        }
        int[] answer = new int[primes.size()];
        for(int i=0; i<primes.size(); i++) answer[i] = primes.get(i);
        return answer;
    }
}