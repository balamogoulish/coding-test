from sys import stdin

n = int(stdin.readline())
switchArr = list(map(int, stdin.readline().split()))
m = int(stdin.readline())

def switch(id):
    if switchArr[id]==0:
        switchArr[id]=1
    else:
        switchArr[id]=0

for _ in range(m):
    s, x = map(int, stdin.readline().split())
    if s == 1: #남자인 경우
        i = 1
        while x*i<=n:
            switch(x*i-1)
            i+=1
    else: #여자인 경우
        i=1
        switch(x-1)
        while True:
            if x-i-1>=0 and x+i<=n:
                prev = x-i-1
                nxt = x+i-1
                i+=1
                if switchArr[prev]==switchArr[nxt]:
                    switch(prev)
                    switch(nxt)
                else:
                    break
            else:
                break

cnt = 0
for a in switchArr:
    print(a, end=' ')
    cnt+=1
    if cnt==20:
        cnt=0
        print()
