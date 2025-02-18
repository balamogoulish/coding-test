'''
1. 지훈이가 현재 위치(단 현재 F가 아닌 경우)에서 상하좌우 불이 안 번진 곳(.)으로 이동
    => 지훈이가 그래프 밖으로 나가면 성공
    => 갈 곳이 없으면 IMPOSSIBLE
2. 불이 상하좌우로 번짐(J, .) 
'''

from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().split())
jh = deque([])
fires = deque([])
graph = [[0 for _ in range(c)] for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited_jh = [[False for _ in range(c)] for _ in range(r)]
visited_fires = [[False for _ in range(c)] for _ in range(r)]

for y in range(r):
    row = stdin.readline().strip()
    for x in range(c):
        graph[y][x] = row[x]
        if row[x] == "J":
            jh.append([x, y])
        elif row[x] == "F":
            fires.append([x, y])

answer = 0

while jh:
    answer+=1
    tmp_fires = deque([])
    while fires:
        cx, cy = fires.popleft()
        for k in range(4):
            nx, ny = cx+dx[k], cy+dy[k]
            if 0<=nx<c and 0<=ny<r and not visited_fires[ny][nx] and graph[ny][nx]!='#' :
                visited_fires[ny][nx] = True
                graph[ny][nx] = "F"
                tmp_fires.append([nx, ny])
    fires = tmp_fires
    tmp_jh = deque([])
    while jh:
        cx, cy = jh.popleft()
        for k in range(4):
            nx, ny = cx+dx[k], cy+dy[k]
            if ny<0 or ny>=r or nx<0 or nx>=c:
                print(answer)
                exit()
            if not visited_jh[ny][nx] and graph[ny][nx]=='.': #방문한 적 없고 불이 아직 번지지 않은 경우 
                visited_jh[ny][nx] = True
                tmp_jh.append([nx, ny])
    jh = tmp_jh


print('IMPOSSIBLE')