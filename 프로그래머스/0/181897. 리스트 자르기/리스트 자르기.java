import java.util.*;

class Solution {
    public List<Integer> solution(int n, int[] slicer, int[] num_list) {
        List<Integer> numList = new ArrayList<>();
        for (int num : num_list) {
            numList.add(num);
        }

        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];

        switch (n) {
            case 1:
                return new ArrayList<>(numList.subList(0, b + 1));
            case 2:
                return new ArrayList<>(numList.subList(a, numList.size()));
            case 3:
                return new ArrayList<>(numList.subList(a, b + 1));
            case 4:
                List<Integer> list = new ArrayList<>();
                for (int i = a; i <= b; i += c) {
                    list.add(num_list[i]);
                }
                return list;
            default:
                return Collections.emptyList();
        }
    }
}