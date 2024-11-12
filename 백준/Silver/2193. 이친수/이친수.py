from sys import stdin

n = int(stdin.readline())

#이친수
# 1 10 100 101 1000 1001 1010 10000 10001 10010 10100 10101 100000 100001 100010 100100 101000 101001 101010 100101
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] +dp[i-2]

print(dp[n])