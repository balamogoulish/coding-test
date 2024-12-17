from sys import stdin

n = int(stdin.readline().strip())
cows = [[1000, 1000] for i in range(10)]
ans = 0
for _ in range(n):
    c, p = map(int, stdin.readline().split(' '))
    if cows[c-1][0]==1000: #최초 등장
        cows[c-1][0]=p
        cows[c-1][1]=0
    elif cows[c-1][0]!=p: #위치 변경됨
            cows[c-1][0]=p
            cows[c-1][1]+=1
for c in cows:
    if c[1]!=1000:
        ans+=c[1]
print(ans)