from sys import stdin

h, y = map(int, stdin.readline().split())

dp = [0]*100
dp[0] = h
gain = [[1, 1.05], [3, 1.2], [5, 1.35]]
for i in range(y+1):
    for g in gain:
        if i+g[0]<=y:
            dp[i+g[0]] = max(dp[i+g[0]], dp[i]*g[1])
            dp[i+g[0]]=int(str(dp[i+g[0]]).split('.')[0])
print(dp[y])
