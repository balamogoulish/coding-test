from sys import stdin

n = int(stdin.readline())

dp = [0]*(1000000)
dp[0] = 1
dp[1] =1

for i in range(2, n+1):
    dp[i] = (1+dp[i-1]+dp[i-2])%1000000007

print(dp[n])