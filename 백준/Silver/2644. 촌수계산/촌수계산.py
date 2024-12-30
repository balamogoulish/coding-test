from collections import deque
from sys import stdin

n = int(stdin.readline())
target1, target2 = map(int, stdin.readline().split())
m = int(stdin.readline())
family = {}
visited = [False for _ in range(n)]

for i in range(n):
    family[i+1] = []
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    family[x].append(y)
    family[y].append(x)

def bfs(p1,p2):
    q = deque([(p1, 0)])
    while q:
        curr = q.popleft()
        visited[curr[0]-1]=True
        # print('----------curr:', curr)
        for nxt in family[curr[0]]:
            if nxt == p2:
                return curr[1]+1
            if not visited[nxt-1]:
                # print('nxt:', nxt, 'cnt:', curr[1]+1)
                q.append((nxt, curr[1]+1))
    return -1
print(bfs(target1, target2))