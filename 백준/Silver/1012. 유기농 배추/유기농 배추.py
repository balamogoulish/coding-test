from sys import stdin
import sys

sys.setrecursionlimit(10**6)

T = int(stdin.readline())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for _ in range(T):
    m, n, k = map(int, stdin.readline().split())
    ground = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = 0
    
    def dfs(x, y):
        visited[y][x] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and ground[ny][nx]==1:
                dfs(nx, ny)
    
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        ground[y][x] = 1
    
    for y in range(n):
        for x in range(m):
            if visited[y][x] or ground[y][x]==0:
                continue
            else:
                answer+=1
                dfs(x, y)
    print(answer)
    