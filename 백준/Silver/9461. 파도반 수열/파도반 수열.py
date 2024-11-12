from sys import stdin

t = int(stdin.readline())
arr = []
for _ in range(t):
    arr.append(int(stdin.readline()))

#1, 1, 1, 2(1+1), 2(1+1) ,3(1+2) , 4(2+2), 5(2+3), 7(3+4), 9(4+5)
dp = [0]*(max(arr)+1)
dp[1] = 1
dp[2] = 1

for i in range(3, max(arr)+1):
    dp[i] = dp[i-3]+dp[i-2]
for a in arr:
    print(dp[a])
    