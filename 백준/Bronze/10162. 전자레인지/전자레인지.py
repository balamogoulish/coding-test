from sys import stdin

t = int(stdin.readline())
btn = [300, 60, 10]
ans=[]

for b in btn:
    ans.append(t//b)
    t=t%b

if t==0:
    for a in ans:
        print(a, end=' ')
else:
    print(-1)