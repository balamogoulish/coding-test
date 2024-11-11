from sys import stdin

n = int(stdin.readline())
dp = [0]*(abs(n)+1)

if len(dp)>1:
    dp[1] = 1

for i in range(2, abs(n)+1):
    dp[i] = (dp[i-2]+dp[i-1])%1000000000
    
if n<0 and n%2==0:
    print(-1)
elif n==0:
    print(0)
else:
    print(1)
print(abs(dp[abs(n)]))
        