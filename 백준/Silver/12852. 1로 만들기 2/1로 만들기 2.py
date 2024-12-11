from sys import stdin

x = int(stdin.readline())
dp = [0]*(x+1) 
route = [0]*(x+1)
answer = [x]
for i in range(2, x+1):
    dp[i]=dp[i-1]+1
    route[i]=i-1
    if i%2 == 0 and dp[i//2]+1<=dp[i]:
        dp[i] = dp[i//2]+1
        route[i]=i//2
    if i%3 == 0 and dp[i//3]+1<=dp[i]:
        dp[i] = dp[i//3]+1
        route[i]=i//3

print(dp[x])
i=x
while i!=1:
    i = route[i]
    answer.append(i)
for a in answer:
    print(a, end=' ')