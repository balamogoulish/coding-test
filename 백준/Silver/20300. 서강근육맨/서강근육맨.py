from sys import stdin
from collections import deque

n = int(stdin.readline())
health = sorted(list(map(int, stdin.readline().split())))
q = deque(health)

max_h = 0

if n%2==1:
    max_h = q.pop()
while q:
    max_h = max(max_h, q.pop()+q.popleft())
print(max_h)
