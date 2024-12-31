from sys import stdin
import sys

sys.setrecursionlimit(10**6)

n, m, k = map(int, stdin.readline().split())
trash = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = [0, 0]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(k):
    r, c = map(int, stdin.readline().split())
    trash[r-1][c-1] = 1

def dfs(x, y):
    answer[1]+=1
    visited[y][x] = True
    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y
        if 0<=nx<m and 0<=ny<n:
            if trash[ny][nx]==1 and not visited[ny][nx]:
                dfs(nx, ny)
            
for y in range(n):
    for x in range(m):
        if not visited[y][x] and trash[y][x]==1:
            answer[1]=0
            dfs(x, y)
            answer[0] = max(answer[0], answer[1])
print(answer[0])
            
