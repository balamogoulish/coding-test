import java.util.*;
import java.util.stream.*;

class Solution {
    public String[] solution(String my_string) {
        return Arrays.stream(my_string.trim().split(" "))
                     .filter(s -> !s.isBlank())  // 공백 제거
                     .toArray(String[]::new);    // 배열로 변환
    }
}