'''
n*m 행렬
부분 행렬의 합의 최댓값
1. 부분합 구하기
sum[i][j] = arr[0][0] + ... + arr[i-1][j-1] 
sum[i][j] = arr[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

2. 구간합 구하기
S = sum[x2+1][y2+1] - sum[x1][y2+1] - sum[x2+1][y1] + sum[x1+1][y1+1] 
'''

from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

sum_board = [[0 for _ in range(m+1)] for _ in range(n+1)]
sum_board[1][1] = board[0][0]
#부분 합 구하기 
for i in range(1, n+1):
    for j in range(1, m+1):
        sum_board[i][j] = board[i-1][j-1] + sum_board[i-1][j] + sum_board[i][j-1] - sum_board[i-1][j-1]

answer = board[0][0]

for y1 in range(n): 
    for y2 in range(y1, n):
        for x1 in range(m):
            for x2 in range(x1, m):
                answer = max(answer,
                    sum_board[y2+1][x2+1]- sum_board[y2+1][x1] - sum_board[y1][x2+1] + sum_board[y1][x1]
                )
                
print(answer)