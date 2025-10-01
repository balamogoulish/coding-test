class Solution {
    public int solution(int[] array) {
        int[] tmp = new int[array.length];
        sort(array, tmp, 0, array.length - 1);

        // 중앙값(정렬 후)
        return array[array.length / 2];
    }

    private void sort(int[] arr, int[] tmp, int left, int right) {
        if (left >= right) return;

        int mid = (left + right) >>> 1;
        sort(arr, tmp, left, mid);
        sort(arr, tmp, mid + 1, right);

        merge(arr, tmp, left, mid, right);
    }

    private void merge(int[] arr, int[] tmp, int left, int mid, int right) {
        for (int i = left; i <= right; i++) tmp[i] = arr[i];

        int l = left;      // 왼쪽 시작
        int r = mid + 1;   // 오른쪽 시작
        int idx = left;    // arr에 채워 넣을 위치

        // 2) tmp에서 꺼내 arr로 병합
        while (l <= mid && r <= right) {
            if (tmp[l] <= tmp[r]) arr[idx++] = tmp[l++];
            else                   arr[idx++] = tmp[r++];
        }

        while (l <= mid) arr[idx++] = tmp[l++];
        while (r <= right) arr[idx++] = tmp[r++];
    }
}
