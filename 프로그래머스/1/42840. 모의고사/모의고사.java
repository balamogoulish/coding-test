import java.util.*;

class Solution {
    public List<Integer> solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        int[] scores = new int[3];
        int[][] results = {
            {1, 2, 3, 4, 5},
            {2, 1, 2, 3, 2, 4, 2, 5},
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        
        for(int i=0; i<3; i++){
            int score = 0;
            for(int j=0; j<answers.length; j++){
                if(results[i][j%results[i].length] == answers[j]) score++;
            }
            scores[i] = score;
        }
        
        int max_score = Arrays.stream(scores).max().getAsInt();
        for(int i=0; i<3; i++){
            if(scores[i] >= max_score) answer.add(i+1);
        }
        
        return answer;
    }
}