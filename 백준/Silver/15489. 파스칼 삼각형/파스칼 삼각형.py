from sys import stdin

r, c, w = map(int, stdin.readline().split())

#[1]
#[1, 1]
#[1, 2, 1]
#[1, 3, 3, 1]
#1. n번째 줄의 요소는 n개를 갖는다
#2. n번째 줄의 i번째 요소는 n-1번째 줄의 i-1, i번째 요소의 합이다.
#3. 파스칼 삼각형은 데칼코마니다.

dp = [[1], [1, 1]]
answer = 0

for i in range(2, r+w-1):
    dp.append([1]*(i+1))
    for j in range(1, i):
       dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

for i in range(w):
    answer+=sum(dp[r+i-1][c-1:c+i])
    #i=0일때는 c-1을 기준으로 1개 => dp[r+i-1][c-1:c-1+1]
    #i=1일때는 c-1을 기준으로 오른쪽으로 2개 dp[r+i-1][c-1:c-1+2]
print(answer)