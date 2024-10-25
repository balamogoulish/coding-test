from sys import stdin

s = int(stdin.readline())

ans = 0
temp = 0
for i in range(1, s):
    temp+=i
    ans+=1
    if s-temp <= i:
        print(ans)
        break
if s==1:
    print(1)