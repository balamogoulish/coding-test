from sys import stdin
import sys

sys.setrecursionlimit(10**6) 

n = int(stdin.readline())
RGB = [[rgb for rgb in stdin.readline().strip()] for _ in range(n)] #적록색맹 X
RB = [] #적록색맹 O => G를 모두 R로 변환 
rgb = 0 #적록색맹이 아닌 사람이 본 구역
rb = 0 #적록생맹인 사람이 본 구역
visited_rgb = [[0 for _ in range(n)] for _ in range(n)]
visited_rb = [[0 for _ in range(n)] for _ in range(n)]
answer= [0, 0]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in RGB:
    tmp = []
    for j in i:
        if j=='G':
            tmp.append('R')
        else:
            tmp.append(j)
    RB.append(tmp)

def dfs_rb(x, y, color):
    visited_rb[y][x] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and color == RB[ny][nx] and not visited_rb[ny][nx]:
            dfs_rb(nx, ny, color)
def dfs_rgb(x, y, color):
    visited_rgb[y][x] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and color == RGB[ny][nx] and not visited_rgb[ny][nx]:
            dfs_rgb(nx, ny, color)

for y in range(n):
    for x in range(n):
        if visited_rb[y][x]==0:
            answer[1]+=1
            dfs_rb(x, y, RB[y][x])
        if visited_rgb[y][x]==0:
            answer[0]+=1
            dfs_rgb(x, y, RGB[y][x])

for p in answer:
    print(p, end=' ')