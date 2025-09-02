import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int S = sc.nextInt(); // DNA 문자열 길이
        int P = sc.nextInt(); // 부분 문자열 길이
        char[] dna = sc.next().toCharArray(); //DNA 문자열
        HashMap<Character, Integer> limits = new HashMap<>(); // A C G T의 최소 개수
        limits.put('A', sc.nextInt());
        limits.put('C', sc.nextInt());
        limits.put('G', sc.nextInt());
        limits.put('T', sc.nextInt());

        HashMap<Character, Integer> counts = new HashMap<>();
        counts.put('A', 0);
        counts.put('C', 0);
        counts.put('G', 0);
        counts.put('T', 0);
        for(int i=0; i<P; i++){
            counts.replace(dna[i], counts.get(dna[i])+1);
        }

        int start = 0;
        int end = P-1;
        while(end<S){
            boolean success = true;
            for(Character key: counts.keySet()){
                if(counts.get(key)<limits.get(key)){
                    success = false;
                    break;
                }
            }
            if(success){
                answer++;
            }
            if(end==S-1){
                break;
            }
            char s = dna[start];
            counts.replace(s, counts.get(s)-1);
            char e = dna[end+1];
            counts.replace(e, counts.get(e)+1);
            start++;
            end++;


        }
        System.out.println(answer);
    }
}
