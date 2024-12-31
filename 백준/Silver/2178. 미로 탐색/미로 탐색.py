from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split()) #n:y, m:x
maze = [[int(a) for a in stdin.readline().strip()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx= [1, 0, -1, 0]
dy= [0, 1, 0, -1]

def bfs(x, y):
    visited[y][x] = 1
    q = deque([[x, y, 1]])
    while q:
        curr_x, curr_y, curr_cnt = q.popleft()
        for i in range(4):
            nx, ny = curr_x+dx[i], curr_y+dy[i]
            if 0<=nx<m and 0<=ny<n and maze[ny][nx]==1:
                if visited[ny][nx]==False or visited[ny][nx]>curr_cnt+1:
                    visited[ny][nx] = curr_cnt+1
                    q.append([nx, ny, curr_cnt+1])
bfs(0, 0)
print(visited[n-1][m-1])