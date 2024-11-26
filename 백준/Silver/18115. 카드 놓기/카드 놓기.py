from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = deque(list(map(int, stdin.readline().split())))
floor = deque([i for i in range(1, n+1)])
init = deque([])
    
while arr:
    act = arr.pop()
    if act==1: 
        x = floor.popleft()
        init.appendleft(x)
    elif act==2:
        x = floor.popleft()
        y = init.popleft()
        init.appendleft(x)
        init.appendleft(y)
    elif act==3:
        x = floor.popleft()
        init.append(x)
for i in init:
    print(i, end=' ')