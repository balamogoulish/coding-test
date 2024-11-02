from sys import stdin

n = int(stdin.readline())
dp = [1000001]*(n+1)
if n>1:
    dp[2] = 1
    if n>4:
        dp[5] = 1

for i in range(n+1):
    if dp[i]==1000001:
        continue
    if i+2<=n:
        dp[i+2] = min(dp[i]+1, dp[i+2])
    if i+5<=n:
        dp[i+5] = min(dp[i]+1, dp[i+5])
if dp[n]==1000001:
    print(-1)
else:
    print(dp[n])