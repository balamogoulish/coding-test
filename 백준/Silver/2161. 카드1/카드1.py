from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = deque([i for i in range(1, n+1)])
ans = []
while len(arr)>1:
    ans.append(arr.popleft())
    if len(arr)==1:
        break
    arr.append(arr.popleft())
ans.append(arr.pop())

for a in ans:
    print(a, end=' ')