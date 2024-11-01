from sys import stdin

x = int(stdin.readline())
dp = [0]*(x+1) #1~x까지 각 1까지 가기 위해서 필요한 연산 최소 횟수를 담는 배열열

for i in range(2, x+1):
    cnt = dp[i-1]+1
    if i%3==0: #3으로 나뉘는 경우
        cnt = min(cnt, dp[i//3]+1)
    if i%2==0:
        cnt = min(cnt, dp[i//2]+1)
    dp[i] = cnt
print(dp[x])