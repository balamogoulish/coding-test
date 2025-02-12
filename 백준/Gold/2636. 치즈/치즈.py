from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
cheese_cnt = 0

# 전체 치즈 개수 계산
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            cheese_cnt += 1

# BFS를 통해 공기 영역을 찾아 치즈를 녹임
def bfs(visited, n, m):
    visited[0][0] = True
    dq = deque([[0, 0]])
    melt = []  # 녹일 치즈를 담을 리스트
    while dq:
        cx, cy = dq.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == 1:  # 0 옆에 1이 있으면 녹일 치즈에 추가
                    melt.append([nx, ny])
                else:
                    dq.append([nx, ny])
    
    # 녹인 치즈를 녹이기
    for mx, my in melt:
        graph[my][mx] = 0

    return len(melt)

hour = 0
while cheese_cnt > 0:
    visited = [[False] * m for _ in range(n)]  # 방문 여부 체크를 위한 visited 초기화
    melted_cheese_cnt = bfs(visited, n, m)
    hour += 1
    cheese_cnt -= melted_cheese_cnt
    
    if cheese_cnt == 0:
        print(hour)
        print(melted_cheese_cnt)  # 마지막 시간과 녹인 치즈 개수 출력
        break
