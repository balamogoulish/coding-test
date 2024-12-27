from sys import stdin
import sys

sys.setrecursionlimit(10**6)

m, n, k = map(int, stdin.readline().split())
box = [[1 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
tmp = [0]
answer = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(k):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            box[y][x]=0

def bfs(x, y):
    visited[y][x]=True
    tmp[0]+=1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[ny][nx] and box[ny][nx]==1:
            bfs(nx, ny)

for y in range(m):
    for x in range(n):
        if not visited[y][x] and box[y][x]==1:
            tmp[0]=0
            bfs(x, y)
            answer+=tmp
print(len(answer))
for a in sorted(answer):
    print(a, end=' ')