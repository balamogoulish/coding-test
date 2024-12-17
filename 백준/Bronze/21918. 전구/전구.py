from sys import stdin

n, m = map(int, stdin.readline().split())
s = list(map(int, stdin.readline().split()))

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        s[b-1]=c
    elif a == 2:
        for i in range(b-1, c):
            if s[i]==1:
                s[i]=0
            else:
                s[i]=1
    elif a==3:
        for i in range(b-1, c):
            s[i]=0
    else:
        for i in range(b-1, c):
            s[i]=1
for x in s:
    print(x, end=' ')
        
