from sys import stdin

n = int(stdin.readline())
# t(0)=1
# t(1)=1
# t(2)=2
# t(3)=5
# t(4)=1*5+2*1+1*2+5*1=14
# t(5)=1*14+5*1+2*2+5*1+14*1=28+10+4=42
# t(n)=t(0)*t(n-1)+t(1)*t(n-2)+...+t(n-1)*t(0)
dp = [0]*(n+1)
dp[0]=1

for i in range(1, n+1): 
    for j in range(i+1): 
        #i=3일때, j=0~2 => (0, 2),(1, 1),(0, 0) => j==i-j이면 더하기 전에 *2하고 마지막에 j==i-j인 dp를 한 번 더함 
        #i=4일때, j=0~3 => (0, 3),(1, 2),(2, 1) => j<i-j이면 더하기 전에 *2하고 return
        if j>=i-j-1:
            dp[i]*=2
            if j==i-j-1:
                dp[i]+=dp[j]*dp[i-j-1]
            break
        dp[i] += dp[j]*dp[i-j-1]
print(dp[n])