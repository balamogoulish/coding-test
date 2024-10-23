#https://www.acmicpc.net/problem/1436

arr = set([66600, 666000, 6660000])
ans = 0

n = int(input())
i=666
while True:
    if '666' in str(i):
        ans+=1
        if ans==n:
            print(i)
            break
    i+=1
