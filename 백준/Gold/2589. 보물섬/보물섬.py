from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
maps = [[a for a in stdin.readline().strip()] for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
dist = [[0 for _ in range(m)] for _ in range(n)]

def bfs(x, y, d):
    q =deque([[x, y, d]])
    visited[y][x] = True
    max_dist = 0
    while q:
        curr_x, curr_y, curr_d = q.popleft()
        max_dist = max(max_dist, curr_d)
        for i in range(4):
            nx, ny = curr_x+dx[i], curr_y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and maps[ny][nx]=='L':
                dist[ny][nx] = curr_d+1
                visited[ny][nx] = True
                q.append([nx, ny, curr_d+1])
    return max_dist

answer = 0
for y in range(n):
    for x in range(m):
        if maps[y][x]=='L':
            visited = [[False for _ in range(m)] for _ in range(n)]
            answer = max(answer, bfs(x, y, 0))
print(answer)

            