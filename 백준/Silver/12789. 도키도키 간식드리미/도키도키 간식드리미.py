from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = deque(list(map(int, stdin.readline().split())))
wait = []
ans = 'Nice'

min_arr=1
for i in range(n):
    x=arr.popleft()
    if x!=min_arr:
        while len(wait)!=0 and wait[-1]==min_arr:
            wait.pop()
            min_arr+=1
        wait.append(x)
    else:
        min_arr+=1

for _ in range(len(wait)):
    min_wait = min(wait)
    x=wait.pop()
    if x!=min_wait:
        ans = 'Sad'
        break
print(ans)