from sys import stdin

T = int(stdin.readline())
dp = [0]*12
dp[1] =1
dp[2] =1
dp[3] =1

for i in range(12):
    if i+1<12:
        dp[i+1]+=dp[i]
    if i+2<12:
        dp[i+2]+=dp[i]
    if i+3<12:
        dp[i+3]+=dp[i]

for _ in range(T):
    n = int(stdin.readline())
    print(dp[n])
