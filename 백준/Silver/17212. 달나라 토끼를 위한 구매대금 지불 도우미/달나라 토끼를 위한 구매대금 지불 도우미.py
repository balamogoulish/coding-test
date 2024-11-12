from sys import stdin

n = int(stdin.readline())

dp = [100001]*(100001)
dp[0]=0
coins = [1, 2, 5, 7]

for i in range(n+1):
    for c in coins:
        if i+c<=n:
            dp[i+c] = min(dp[i+c], dp[i]+1)
print(dp[n])