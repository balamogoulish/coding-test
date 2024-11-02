from sys import stdin

n = int(stdin.readline())

turn = 'SK' #'SK'와 'CY'를 번갈아 가면서 할당함
dp = [1001]*(n+1)
dp[0] = 0

for i in range(n+1):
    if i+1<=n:
        dp[i+1] = min(dp[i]+1, dp[i+1])
    if i+3<=n:
        dp[i+3] = min(dp[i]+1, dp[i+3])
if dp[n]%2==0:
    print('CY')
else:
    print('SK')