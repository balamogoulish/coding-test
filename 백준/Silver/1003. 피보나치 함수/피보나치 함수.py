from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    dp = [[0, 0]]*(n+1)
    # 0호출 시 => 1, 0
    # 1호출 시 => 0, 1
    # 2호출 시 => 0호출 시 + 1호출 시
    # 3호출 시 => 1호출 시 + 2호출 시
    if n==0:
        print(1, 0)
        continue
    if n==1:
        print(0, 1)
        continue
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, n+1):
        zero = dp[i-1][0] + dp[i-2][0]
        one = dp[i-1][1] + dp[i-2][1]
        dp[i] = [zero, one]
    print(dp[n][0], dp[n][1])