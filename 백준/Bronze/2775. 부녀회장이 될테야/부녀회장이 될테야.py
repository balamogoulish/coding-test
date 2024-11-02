# k층 n호
# 0층 => 1, 2, 3, ... , n
# 1층 => 1, 1+2, 1+2+3, 1+2+3+4, ... , 1+2+...+n
# 2층 => 1, 1+1+2, 1+1+1+2+2+3, 1+1+1+1+2+2+2+3+3+4, ... , 1*n+2*(n-1)+...+n
# 3층 => 1, 1+1+1+2, 1+1+1+1+1+1+2+2+2+3, 1+1+1+1+1+1+1+1+1+1+2+2+2+2+2+2+3+3+3+4, ..., 

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())
    dp = [i for i in range(1, n+1)]
    for i in range(1, k+1):
        for j in range(1, n):
            dp[j] += dp[j-1]

    print(dp[n-1])