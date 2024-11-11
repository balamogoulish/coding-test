from sys import stdin

n = int(stdin.readline())
dp = [5]*(n+1)
dp[0] = 0
for i in range(n+1):
    for j in range(1, int(n**(0.5))+1):
        if i+j**2<(n+1):
            dp[i+j**2] = min(dp[i+j**2], dp[i]+1)

print(dp[n])