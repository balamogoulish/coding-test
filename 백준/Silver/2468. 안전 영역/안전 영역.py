from sys import stdin
import sys

sys.setrecursionlimit(10**7)

n = int(stdin.readline())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
max_h = 0
answers = []

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for m in maps:
    max_h = max(max_h, max(m))
    
def dfs(x, y, h):
    visited[y][x] = True
    for  i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[ny][nx] and maps[ny][nx]>h:
                dfs(nx, ny, h)
                
    
for i in range(max_h):
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = 0
    for curr_y in range(n):
        for curr_x in range(n):
            if not visited[curr_y][curr_x] and maps[curr_y][curr_x]>i:
                answer+=1
                dfs(curr_x, curr_y, i)
    answers.append(answer)
print(max(answers))