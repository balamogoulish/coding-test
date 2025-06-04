# cnt[i][j]: j번째 계단을 연속되게 i번 밟음
# cnt[0][j]: cnt[0][j-2], cnt[1][j-2], cnt[2][j-2]
# cnt[1][j]: cnt[0][j-1]

from sys import stdin

def solution():
    n = int(stdin.readline())
    scores = [int(stdin.readline()) for _ in range(n)]
    cnt = [[s for s in scores] for _ in range(2)]
    
    
    if n<3:
        return sum(scores)
    else:
        cnt[1][1] = cnt[0][0]+cnt[0][1]
        for j in range(2, n):
            cnt[1][j] = cnt[0][j]+cnt[0][j-1]
            cnt[0][j] = max(cnt[0][j-2]+cnt[0][j], cnt[1][j-2]+cnt[0][j])
        
        return max(cnt[0][n-1], cnt[1][n-1])
    
print(solution())