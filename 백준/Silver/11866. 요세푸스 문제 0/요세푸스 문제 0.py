from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
arr= deque([i for i in range(1, n+1)])

x = 0
ans=''
while len(arr)!=0:
    x+=1
    curr = arr.popleft()
    if x==k:
        x=0
        ans+=str(curr)+', '
    else:
        arr.append(curr)
print('<'+ans[:-2]+'>')