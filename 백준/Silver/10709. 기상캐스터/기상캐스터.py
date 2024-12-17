from sys import stdin
from collections import deque

h, w = map(int, stdin.readline().split())
clouds = []
answer = []

for i in range(h):
    clouds.append(deque(list(stdin.readline().strip())))
    answer.append([-1]*w)

for i in range(w):
    for y in range(h):
        for x in range(w):
            if clouds[y][x]=='c' and answer[y][x]==-1:
                answer[y][x]=i
        clouds[y].appendleft('.')
for ans in answer:
    for a in ans:
        print(a, end=' ')
    print()