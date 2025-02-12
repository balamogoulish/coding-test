'''
세로 n, 가로 m 인 연구소 lab
lab[y][x] = 0: 방
lab[y][x] = 1: 벽
lab[y][x] = 2: 바이러스

3개의 벽(1)을 세웠을 때 안전 영역의 최대 크기

1. 벽 세우기 (3개)
    영역 구하기
    1. 바이러스 퍼뜨리기 (bfs)
    2. 안전 영역 구하기 (bfs)

2. 안전 영역 최댓값 구하기
'''
from sys import stdin
from collections import deque
from itertools import combinations

n, m = map(int, stdin.readline().split())
lab = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
answer = []
viruses_loc = []
walls = []
for y in range(n):
    for x in range(m):
        if lab[y][x]==2:
            viruses_loc.append([x, y])
        elif lab[y][x]==1:
            walls.append([x, y])

def get_safe_zone():
    visited = [v for v in viruses_loc]
    viruses = deque([v for v in viruses_loc])
    
    while viruses:
        cx,cy = viruses.popleft()
        for k in range(4):
            nx, ny = dx[k]+cx, dy[k]+cy
            if 0<=nx<m and 0<=ny<n and [nx, ny] not in visited and lab[ny][nx]!=1:
                viruses.append([nx, ny])
                visited.append([nx, ny])
    # print("========",n*m-len(visited)-len(walls)-3)
    # for l in lab:
    #     print(l)
    answer.append(n*m-len(visited)-len(walls)-3)

def make_wall():
    coordinates = [[x, y] for x in range(m) for y in range(n)]
    
    for new_walls in combinations(coordinates, 3):
        if new_walls[0] in walls or new_walls[1] in walls or new_walls[2] in walls:
            continue
        if lab[new_walls[0][1]][new_walls[0][0]]==2 or lab[new_walls[1][1]][new_walls[1][0]]==2 or lab[new_walls[2][1]][new_walls[2][0]]==2:
            continue
        for wall in new_walls:
            x, y = wall
            lab[y][x] = 1
        get_safe_zone()
        for wall in new_walls:
            x, y = wall
            lab[y][x] = 0
make_wall()
print(max(answer))
    