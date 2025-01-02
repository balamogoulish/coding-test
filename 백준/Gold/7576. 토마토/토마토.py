from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
box = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
q = deque([])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(q):
    while q:
        curr_x, curr_y, cnt = q.popleft()
        for i in range(4):
            nx, ny =curr_x+dx[i], curr_y+dy[i]
            if 0<=nx<m and 0<=ny<n and box[ny][nx]==0:
                if visited[ny][nx]==-1 or visited[ny][nx]>cnt+1:
                    visited[ny][nx]=cnt+1
                    q.append([nx, ny, cnt+1])

for y in range(n):
    for x in range(m):
        if visited[y][x]==-1 and box[y][x]==1:
            q.append([x, y, 0])
            visited[y][x]=0
bfs(q)

answer=0            
for y in range(n):
    for x in range(m):
        if box[y][x]!=-1 and visited[y][x]==-1:
            print(-1)
            exit()
        answer = max(answer, visited[y][x])
print(answer)
            